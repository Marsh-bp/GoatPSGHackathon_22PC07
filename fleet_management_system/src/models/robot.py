import math
from utils.helpers import log_event

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
        if len(path) < 2:  
            log_event(f"Robot {self.id}: Invalid path assigned {path}.")
            self.state = "idle"
            return
        self.target_path = path[1:] 
        self.current_lane = (path[0], path[1])
        self.state = "moving"
        self.move_progress = 0
        log_event(f"Robot {self.id}: Assigned path {path}")


    def update(self):
        if self.state == "moving":
            if self.current_lane is None:
                self.state = "idle"
                log_event(f"Robot {self.id}: No current lane, now idle.")
                return

            if self.move_progress == 0 and not self.traffic_manager.request_lane(self.id, *self.current_lane):
                self.state = "waiting"
                log_event(f"Robot {self.id}: Waiting for lane {self.current_lane}.")
                return

            self.move_progress += self.speed
            if self.move_progress >= 1:  
                self.arrive_at_vertex()
                return

            start_pos = self.nav_graph.vertices[self.current_lane[0]]["pos"]
            end_pos = self.nav_graph.vertices[self.current_lane[1]]["pos"]
            self.pos[0] = start_pos[0] + (end_pos[0] - start_pos[0]) * self.move_progress
            self.pos[1] = start_pos[1] + (end_pos[1] - start_pos[1]) * self.move_progress
            self.draw()

        elif self.state == "waiting":
            if self.traffic_manager.request_lane(self.id, *self.current_lane):
                self.state = "moving"
                log_event(f"Robot {self.id}: Resuming movement on lane {self.current_lane}.")

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
        self.traffic_manager.release_lane(*self.current_lane) 
        self.current_vertex = self.current_lane[1]  
        self.target_path.pop(0)
        log_event(f"Robot {self.id}: Arrived at vertex {self.current_vertex}.")

        if self.target_path:
            self.current_lane = (self.current_vertex, self.target_path[0])  
            self.move_progress = 0 
        else:
            self.state = "complete"  
            log_event(f"Robot {self.id}: Task completed.")
            for lane_key in list(self.traffic_manager.lane_occupancy.keys()):
                if self.traffic_manager.lane_occupancy[lane_key] == self.id:
                    self.traffic_manager.release_lane(*lane_key)

        self.draw()


    def interpolate_position(self):
            start_pos = self.nav_graph.vertices[self.current_lane[0]]["pos"]
            end_pos = self.nav_graph.vertices[self.current_lane[1]]["pos"]
            self.pos[0] = start_pos[0] + (end_pos[0] - start_pos[0]) * self.move_progress
            self.pos[1] = start_pos[1] + (end_pos[1] - start_pos[1]) * self.move_progress 

    def draw(self):
            x, y = self.pos 
            if not self.gui_item:
                
                self.gui_item = self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
                self.text_item = self.canvas.create_text(x, y, text=str(self.id), fill="white")
            else:
                
                self.canvas.coords(self.gui_item, x - 10, y - 10, x + 10, y + 10)
                self.canvas.coords(self.text_item, x, y)  
    