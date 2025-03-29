class TrafficManager:
    def __init__(self):
        self.lane_occupancy = {}

    def get_lane_key(self,a ,b):
        return tuple(sorted((a,b)))
    
    def request_lane(self, robot_id, a ,b):
        lane_key = self.get_lane_key(a,b)
        if lane_key in self.lane_occupancy:
            return False
        else:
            self.lane_occupancy[lane_key] = robot_id
        return True
    
    def release_lane(self, a,b ):
        lane_key = self.get_lane_key(a,b)
        if lane_key in self.lane_occupancy:
            del self.lane_occupancy[lane_key]