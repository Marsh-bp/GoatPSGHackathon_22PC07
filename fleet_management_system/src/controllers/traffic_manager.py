class TrafficManager:
    def __init__(self):
        self.lane_occupancy = {}

    def get_lane_key(self,a ,b):
        return tuple(sorted((a,b)))
    
    def request_lane(self, robot_id, a, b):
        key = self.get_lane_key(a, b)
        if key in self.lane_occupancy:
            current_holder = self.lane_occupancy[key]
            if current_holder == robot_id:
                return True  
            return False  
        self.lane_occupancy[key] = robot_id
        return True

    
    def release_lane(self, a, b):
        key = self.get_lane_key(a, b)
        if key in self.lane_occupancy:
            del self.lane_occupancy[key]
    
