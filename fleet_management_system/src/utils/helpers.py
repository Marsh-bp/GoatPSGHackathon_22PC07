def log_event(message):
    with open(r"fleet_management_system\src\logs\fleet_logs.txt", "a") as log_file:
        log_file.write(message + "\n")
