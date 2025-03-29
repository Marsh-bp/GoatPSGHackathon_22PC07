class TrafficManager:
    def __init__(self):
        self.lane_occupancy = {}

    def get_lane_key(self,a ,b):
        return tuple(sorted((a,b)))
    
    def request_lane(self, robot_id, a ,b):
        key = self.get_lane_key(a,b)
        if key in self.lane_occupancy:
            return False
        else:
            self.lane_occupancy[key] = robot_id
        return True
    
    def release_lane(self, a,b ):
        key = self.get_lane_key(a,b)
        if key in self.lane_occupancy:
            del self.lane_occupancy[key]