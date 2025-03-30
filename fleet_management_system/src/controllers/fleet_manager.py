from models.robot import Robot
from utils.helpers import log_event, find_path


class FleetManager:
    def __init__(self,nav_graph, traffic_manager, canvas):
        self.robots = []
        self.nav_graph = nav_graph
        self.traffic_manager = traffic_manager
        self.canvas = canvas

    def spawn_robot(self, vertex_index):
        robot_id = len(self.robots) + 1
        robot = Robot(vertex_index, self.nav_graph, self.traffic_manager, self.canvas)
        self.robots.append(robot)
        robot.draw()
        log_event(f"Robot {robot_id}: Spawned at vertex {vertex_index}.")

    def assign_task(self, robot, dest_index):
        path = find_path(robot.current_vertex,dest_index, self.nav_graph)
        if path:
            robot.assign_path(path)
            log_event(f"Robot {robot.id}: Task assigned to move to vertex {dest_index}.")
    
    
    def update_all(self):
        for robot in self.robots:
            robot.update()