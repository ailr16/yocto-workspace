import json
import subprocess

class colors:
    ERROR = "\033[31m",
    OK = "\033[32m"

json_file = open("config.json")

configuration = json.load(json_file)

print("""Verify the data:
      Container ID: {0}
      Container name: {1}
      Output dir in container: {2}
      Output dir in host: {3}
      """.format(configuration["container-name"],
                 configuration["container-id"],
                 configuration["output-dir"],
                 configuration["host-output-dir"]
                 )
)

print("Enter the file name: ")
img_file_name = str(input())


print("Start copying the file:\n {0}{1}\ninto:\n {2}? (y/n)".format(configuration["output-dir"],
                                                           img_file_name,
                                                           configuration["host-output-dir"]))

selection = str(input())

if selection in ['Y', 'y']:
    command = "docker cp {0}:{1}{2} {3}".format(configuration["container-id"],
                                            configuration["output-dir"],
                                            img_file_name,
                                            configuration["host-output-dir"])

    print("Running: " + command)

    return_value = subprocess.run(command, shell=True, capture_output=True, text=True)
    if return_value.returncode == 0:
        print(colors.OK + "Copied!")
    else:
        print(colors.ERROR + "There has been an error!")

elif selection in ['N', 'n']:
    exit()

else:
    print("Invalid selection")