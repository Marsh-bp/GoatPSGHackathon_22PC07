import math
 
class Robot:
    id_counter = 1

    def __init__(self, start_vertex, nav_graph, traffic_manager,canvas):
        self.id = Robot.id_counter
        Robot.id_counter += 1
        self.nav_graph = nav_graph
        self.traffic_manager = traffic_manager
        self.canvas = canvas
        self.current_vertex = start_vertex
        self.path = list(nav_graph.vertices[start_vertex]["pos"])
        self.target_path = []
        self.state = "idle"
        self.move_progress = 0
        self.current_lane = None
        self.speed = 0.02
        self.gui_item = None
    
    def assign_path(self, path):
        if path:
            self.target_path = path[1:]
            self.state = "moving"

    def update(self):
        if self.state == "moving":
            if self.move_progress == 0 and not self.request_lane():
                self.state = "waiting"
                return
            self.move_progress += self.speed
            if self.move_progress >= 1:
                self.arrive_at_vertex()
                return
            self.interpolate_position()
        
        elif self.state == "waiting":
            if self.request_lane():
                self.state = "moving"

    def request_lane(self):
        a, b = self.current_lane
        return self.traffic_manager.request_lane(self.id, a, b)
    
    def arrive_at_vertex(self):
        self.pos = list(self.nav_graph.vertices[self.current_lane[1]]["pos"])
        self.traffic_manager.release_lane(*self.current_lane)
        self.current_vertex = self.current_lane[1]
        self.target_path.pop(0)
        if self.target_path:
            self.current_lane = (self.current_vertex, self.target_path[0])
        else:
            self.state = "complete"

    def interpolate_position(self):
        start_pos = self.nav_graph.vertices[self.current_lane[0]]["pos"]
        end_pos = self.nav_graph.vertices[self.current_lane[1]]["pos"]
        self.pos[0] = start_pos[0] + (end_pos[0] - start_pos[0]) * self.move_progress
        self.pos[1] = start_pos[1] + (end_pos[1] - start_pos[1]) * self.move_progress 

    def draw(self):
        x, y =self.pos
        if not self.gui_item:
            self.gui_item = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")
            self.canvas.create_text(x, y, text=str(self.id), fill="white")
        else:
            self.canvas.coords(self.gui_item, x-10, y-10, x+10, y+10)