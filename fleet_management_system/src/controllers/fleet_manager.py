from src.models.robot import Robot

class FleetManager:
    def __init__(self,nav_graph, traffic_manager, canvas):
        self.robots = []
        self.nav_graph = nav_graph
        self.traffic_manager = traffic_manager
        self.canvas = canvas

    def spawn_robot(self, vertex_index):
        robot = Robot(vertex_index, self.nav_graph, self.traffic_manager, self.canvas)
        self.robots.append(robot)
        robot.draw()
    
    def assign_task(self, robot, dest_index):
        path = self.nav_graph.find_path(robot.current_vertex,dest_index)
        if path:
            robot.assign_path(path)
    
    def update_all(self):
        for robot in self.robots:
            robot.update()