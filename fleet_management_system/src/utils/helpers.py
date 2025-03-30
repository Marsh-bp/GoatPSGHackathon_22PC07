from src.models.nav_graph import NavGraph
from collections import deque

def log_event(message):
    with open(r"fleet_management_system\src\logs\fleet_logs.txt", "a") as log_file:
        log_file.write(message + "\n")

def find_path(start, goal, nav_graph):
    adjacency_list = nav_graph.build_adjacency_list()

    # Initialize BFS queue and visited set
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        # Iterate over neighbors
        for neighbor in adjacency_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

