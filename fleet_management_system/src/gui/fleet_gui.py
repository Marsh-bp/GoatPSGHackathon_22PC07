import math
from tkinter import messagebox

class FleetGUI:
    def __init__(self, root, nav_graph, fleet_manager):
        self.nav_graph = nav_graph
        self.fleet_manager = fleet_manager
        self.canvas = fleet_manager.canvas
        self.selected_robot = None  # Tracks the currently selected robot for task assignment

        # Draw the navigation graph
        self.draw_nav_graph()

        # Bind mouse clicks for interaction
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def draw_nav_graph(self):
        # Draw lanes first (connections between vertices)
        for lane in self.nav_graph.lanes:
            start, end = lane
            start_pos = self.nav_graph.vertices[start]["pos"]
            end_pos = self.nav_graph.vertices[end]["pos"]
            self.canvas.create_line(*start_pos, *end_pos, fill="gray", width=2)

        # Draw vertices (nodes)
        for vertex in self.nav_graph.vertices.values():
            x, y = vertex["pos"]
            color = "green" if vertex.get("is_charger", False) else "orange"
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=color)
            self.canvas.create_text(x, y, text=vertex["name"], fill="black")

    def on_canvas_click(self, event):
    # Check if the click is near an existing robot
        clicked_robot = self.get_robot_at_point(event.x, event.y)
        if clicked_robot:
            # Select the robot for task assignment
            self.selected_robot = clicked_robot
            messagebox.showinfo(
                "Robot Selected",
                f"Robot {clicked_robot.id} selected. Now click on a destination vertex."
            )
            return  # Exit after selecting the robot

        # Check if the click is near a vertex
        clicked_vertex = self.get_vertex_at_point(event.x, event.y)
        if clicked_vertex is not None:
            if self.selected_robot is None:
                # No robot is selected -> Spawn a new robot
                self.fleet_manager.spawn_robot(clicked_vertex)
            else:
                # Robot is selected -> Assign the task
                messagebox.showinfo(
                    "Task Assigned",
                    f"Task assigned to Robot {self.selected_robot.id}. Moving to vertex {clicked_vertex}."
                )
                self.fleet_manager.assign_task(self.selected_robot, clicked_vertex)
                self.selected_robot = None  # Deselect robot after assigning the task


    def get_vertex_at_point(self, x, y):
        # Determine if a vertex is near the click position
        for idx, vertex in self.nav_graph.vertices.items():
            vx, vy = vertex["pos"]
            if math.sqrt((vx - x)**2 + (vy - y)**2) < 20:  # Adjust radius for detection
                return idx
        return None

    def get_robot_at_point(self, x, y):
        # Determine if a robot is near the click position
        for robot in self.fleet_manager.robots:
            rx, ry = robot.pos
            if math.sqrt((rx - x)**2 + (ry - y)**2) < 15:  # Adjust radius for detection
                return robot
        return None
