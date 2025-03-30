class FleetGUI:
    def __init__(self, root, nav_graph, fleet_manager):
        self.root = root
        self.nav_graph = nav_graph
        self.fleet_manager = fleet_manager
        self.selected_robot = None

        self.canvas = self.fleet_manager.canvas

        self.draw_nav_graph()

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def draw_nav_graph(self):
        for lane in self.nav_graph.lanes:
            start, end = lane[:2]
            start_pos = self.nav_graph.vertices[start]["pos"]
            end_pos = self.nav_graph.vertices[end]["pos"]
            self.canvas.create_line(*start_pos, *end_pos, fill="gray", width=2)

        for vertex_id, vertex in self.nav_graph.vertices.items():
            x, y = vertex["pos"]
            color = "green" if vertex.get("is_charger", False) else "orange"
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=color)

            name = vertex.get("name", "")
            if name:
                self.canvas.create_text(x, y, text=name, fill="black")

    
    def get_robot_at_point(self, x, y):
        for robot in self.fleet_manager.robots:
            rx, ry = robot.pos
            if (x - rx) ** 2 + (y - ry) ** 2 <= 100:  
                return robot
        return None

    def get_vertex_at_point(self, x, y):
        for vertex_id, vertex in self.nav_graph.vertices.items():
            vx, vy = vertex["pos"]
            if (x - vx) ** 2 + (y - vy) ** 2 <= 100:  
                return vertex_id
        return None
    def on_canvas_click(self, event):
        clicked_robot = self.get_robot_at_point(event.x, event.y)
        if clicked_robot:
            self.notify_user(f"Robot {clicked_robot.id} selected. Now click on a destination vertex.")
            self.selected_robot = clicked_robot
            return

        clicked_vertex = self.get_vertex_at_point(event.x, event.y)
        if clicked_vertex is not None:
            if self.selected_robot is None:
                self.fleet_manager.spawn_robot(clicked_vertex)
            else:
                self.fleet_manager.assign_task(self.selected_robot, clicked_vertex)
                self.selected_robot = None  

    def notify_user(self, message):
        from tkinter import messagebox
        messagebox.showinfo("Robot Selected", message)
