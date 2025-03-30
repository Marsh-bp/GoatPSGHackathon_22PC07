class NavGraph:
    def __init__(self, graph):
        self.vertices = self.parse_vertices(graph["vertices"])
        self.lanes = self.parse_lanes(graph["lanes"])
        self.adj = self.build_adjacency_list()
    def parse_vertices(self, vertices_raw):
        vertices = {}
        for idx, vertex in enumerate(vertices_raw):
            x, y, properties = vertex
            vertices[idx] = {
                "index": idx,
                "pos": (x * 50, -y * 50),
                "name": properties.get("name",""),
                "is_charger": properties.get("is_charger", False)
            }
        return vertices
    def parse_lanes(self, lanes_raw):
        return [(lane[0], lane[1]) for lane in lanes_raw]
    
    def build_adjacency_list(self):
        adj = {idx: [] for idx in self.vertices}
        for a,b in self.lanes:
            adj[a].append(b)
            adj[b].append(a)
        return adj
    
    