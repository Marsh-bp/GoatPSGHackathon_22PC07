# GoatPSGHackathon_22PC07

1. To load the graph, change the path in main.py:

with open(r"fleet_management_system\data\nav_graph_2.json", "r") as file:
        nav_graph_data = json.load(file)["levels"]["level1"]

in the json.load(file)["levels"]["level1"] change the revelant value mentioned in the json file, for example:

in nav_graph_2.json the values mentioned as levels, l0 
![alt text](image.png)

so mention this value in the code json.load(file)["levels"]["l0"]

2. To run the code use the following command:
# Install dependencies
pip install -r requirements.txt
# Run your visual GUI system
python src/main.py

the requirements.txt contians the needed dependency for the program

3. A GUI will pop up
![alt text](https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22image-1.png%22%2C%22type%22%3A%22image%2Fpng%22%2C%22signedurl_expire%22%3A%222028-03-29T10%3A15%3A43.764Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F5b01027ae39d4c85%2Fimage-1.png%3FExpires%3D1837937744%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3D1G--LJxTE1UK~q7PvFCa~fdOIiAD3C1AulWHHH2-p71ZKYikzdS9hKNyxK-yvsohRVaJSnJxmH8DhylMpNZWkHrFVjuQSmYoVD0cWQUYa0TvqYeHnuv4EWisFSkTPJHq01M4w3UXzBM-k-H4vswW466360CMbWuLrQHh3DFFwDIPqV0MSlbvoC17~UY1RhTuBtSsMFFo5~dC6pUAMAYrZBi1GeHs6fNfXPrPWcZOg2IMa4KCprkgQ5kjVz2SB5rbSUYNZ1M9N9Bvtw4cB38d2hDcUo3HHzUmqRUJ-3hxj5mxoJ1P9yWndi~nLjO4Zz1o2MsfTD3UFbAwDO2W1zoZbA__%22%7D)



here you can select any vertex to spawn new robot
![alt text](image-2.png)

the robot will be mentioned by robot_id (i.e 1,2,3....), you can spawn multiple robots also you can
spawn robots in real-time without interrupting the navigating robots.

4. To assign task

select the robot you want to assign the task
For example we select robot 1, once selected you will get a message box as
![alt text](image-3.png)

then select the destination vertex, Now the robot moves to the destination
![alt text](image-4.png)

5. Collison avoidance: 

The robot will avoid collision with other robots,
if there is a collision, the robot will stop and wait for the other robot to pass by.
![alt text](image-5.png)

6. Logging & Monitoring:
The system logs all the events in a file named "fleet_logs.txt"
All the robot actions will be logged in fleet_logs.txt 
example:
![alt text](image-6.png)
