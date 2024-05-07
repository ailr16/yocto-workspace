import json
import subprocess

json_file = open("config.json")

configuration = json.load(json_file)

port = configuration["serial-settings"]["serial-port"]
speed = configuration["serial-settings"]["baudrate"]

subprocess.call(["sh", "./serial-monitor-script.sh", port, speed])
