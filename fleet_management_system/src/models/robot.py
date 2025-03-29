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
        self.pos = list(nav_graph.vertices[start_vertex]["pos"])
        self.target_path = []
        self.state = "idle"
        self.move_progress = 0
        self.current_lane = None
        self.speed = 0.02
        self.gui_item = None
    
    def assign_path(self, path):
        if path and len(path) > 1:  # Ensure the path is valid
            self.target_path = path[1:]  # Skip the current vertex
            self.current_lane = (path[0], path[1])  # Set the first lane
            self.state = "moving"
            self.move_progress = 0  # Reset progress for the new task
        else:
            print(f"Robot {self.id}: Invalid path assignment.")


    def update(self):
        if self.state == "moving":
            if self.current_lane is None:
                self.state = "idle"
                return

            # Check if the lane is free
            if self.move_progress == 0 and not self.request_lane():
                self.state = "waiting"
                return

            # Move along the lane
            self.move_progress += self.speed
            if self.move_progress >= 1:  # Reached the end of the lane
                self.arrive_at_vertex()
                return

            # Update position
            start_pos = self.nav_graph.vertices[self.current_lane[0]]["pos"]
            end_pos = self.nav_graph.vertices[self.current_lane[1]]["pos"]
            self.pos[0] = start_pos[0] + (end_pos[0] - start_pos[0]) * self.move_progress
            self.pos[1] = start_pos[1] + (end_pos[1] - start_pos[1]) * self.move_progress
            self.draw()

        elif self.state == "waiting":
            # Try again to request the lane
            if self.request_lane():
                self.state = "moving"

    def calculate_total_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            start_pos = self.nav_graph.vertices[path[i]]["pos"]
            end_pos = self.nav_graph.vertices[path[i + 1]]["pos"]
            total_distance += math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
        return total_distance


    def request_lane(self):
        a, b = self.current_lane
        return self.traffic_manager.request_lane(self.id, a, b)
    
 
    def arrive_at_vertex(self):
        self.pos = list(self.nav_graph.vertices[self.current_lane[1]]["pos"])
        self.traffic_manager.release_lane(*self.current_lane)  # Release the lane
        self.current_vertex = self.current_lane[1]  # Update the current vertex
        self.target_path.pop(0)
        
        if self.target_path:
            self.current_lane = (self.current_vertex, self.target_path[0])  # Set next lane
            self.move_progress = 0  # Reset progress for the new lane
        else:
            self.state = "complete"  # Task is finished
            print(f"Robot {self.id}: Task completed.")
        
        self.draw()


    def interpolate_position(self):
        start_pos = self.nav_graph.vertices[self.current_lane[0]]["pos"]
        end_pos = self.nav_graph.vertices[self.current_lane[1]]["pos"]
        self.pos[0] = start_pos[0] + (end_pos[0] - start_pos[0]) * self.move_progress
        self.pos[1] = start_pos[1] + (end_pos[1] - start_pos[1]) * self.move_progress 

    def draw(self):
        x, y = self.pos  # Current position of the robot
        if not self.gui_item:
            # Create new GUI items if they don't exist
            self.gui_item = self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
            self.text_item = self.canvas.create_text(x, y, text=str(self.id), fill="white")
        else:
            # Update the GUI item's position
            self.canvas.coords(self.gui_item, x - 10, y - 10, x + 10, y + 10)
            self.canvas.coords(self.text_item, x, y)  # Update text position to match the robot