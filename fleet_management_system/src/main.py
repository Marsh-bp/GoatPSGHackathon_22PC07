import tkinter as tk
from models.nav_graph import NavGraph
from controllers.fleet_manager import FleetManager
from controllers.traffic_manager import TrafficManager
from gui.fleet_gui import FleetGUI

def main():
    import json
    with open(r"fleet_management_system\data\nav_graph_2.json", "r") as file:
        nav_graph_data = json.load(file)["levels"]["l0"]

    root = tk.Tk()
    root.title("Fleet Management System")

    canvas = tk.Canvas(root, width=1200, height=800, bg="beige")
    canvas.pack()

    nav_graph = NavGraph(nav_graph_data)
    traffic_manager = TrafficManager()
    fleet_manager = FleetManager(nav_graph, traffic_manager, canvas)
    gui = FleetGUI(root, nav_graph, fleet_manager)

    def update_loop():
        fleet_manager.update_all()
        root.after(50, update_loop)

    update_loop()  
    root.mainloop()

if __name__ == "__main__":
    main()