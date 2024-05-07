import json
import subprocess

json_file = open("config.json")

configuration = json.load(json_file)

command = "docker cp {0}:{1}{2} {3}".format(configuration["container-id"],
                                           configuration["output-dir"],
                                           configuration["output-img"],
                                           configuration["host-output-dir"])

print(command)

subprocess.call(command, shell=True)