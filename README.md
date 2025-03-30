# GoatPSGHackathon_22PC07

## 1. To Load the Graph
To load the graph, change the path in `main.py`:

```python
with open(r"fleet_management_system\data\nav_graph_2.json", "r") as file:
    nav_graph_data = json.load(file)["levels"]["level1"]
```

Change the `json.load(file)["levels"]["level1"]` to reflect the relevant values mentioned in the JSON file. For example:

In `nav_graph_2.json`, the values are:
```json
{
    "building_name": "new_site",
    "levels": {
        "l0": {
            "lanes": [
                ...
            ]
        }
    }
}
```

So, you should use:
```python
json.load(file)["levels"]["l0"]
```

---

## 2. To Run the Code
Use the following commands:

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run your visual GUI system**:
   ```bash
   python src/main.py
   ```

The `requirements.txt` file contains all necessary dependencies for the program.

---

## 3. The GUI
When you run the code, a GUI will pop up:

![GUI Interface](image-1.png)

In the GUI, you can select any vertex to spawn a new robot:

![Spawn Robot Interface](image-2.png)

---

## 4. Assigning Tasks
To assign a task:

1. **Select a robot**:
   Once you select a robot, you will get a message box like this:
   ![Select Robot](image-3.png)

2. **Choose the destination vertex**:
   The robot will move to the assigned destination vertex:
   ![Assign Destination](image-4.png)

---

## 5. Collision Avoidance
The robots can avoid collisions with each other. If there is a collision, a robot will stop and wait for others to pass:
![Collision Avoidance Example](image-5.png)

---

## 6. Logging & Monitoring
All robot actions are logged in the file `fleet_logs.txt`. The logs include events such as task assignments, lane usage, and task completions.

**Example log:**
![Log Example](image-6.png)

---
