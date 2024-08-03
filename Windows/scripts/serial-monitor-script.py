import json
import subprocess

json_file = open("config.json")

configuration = json.load(json_file)

port = "/C=" + str(configuration["serial-settings"]["serial-port"]).replace("COM", "")
speed = "/BAUD=" + str(configuration["serial-settings"]["baudrate"])
bin = configuration["serial-settings"]["teraterm-bin"]

subprocess.Popen([bin, port, speed], shell=True)
