import json
import subprocess

class colors:
    ERROR = "\033[31m"
    OK = "\033[32m"

json_file = open("config.json")

configuration = json.load(json_file)

container_output_dir = configuration["container-settings"]["output-dir"]
host_output_dir = configuration["container-settings"]["host-output-dir"]

print("""Verify the data:
      Container ID: {0}
      Container name: {1}
      Output dir in container: {2}
      Output dir in host: {3}
      """.format(configuration["container-settings"]["container-name"],
                 configuration["container-settings"]["container-id"],
                 container_output_dir,
                 host_output_dir
                 )
)


selection = 99

while(selection != 0):
    print("Do you want to change something (1-Output dir in container) (2-Output dir in host) (0-No, just continue)?")
    selection = int(input())

    if selection == 1:
        print("Enter the new Output directory in container (remeber adding the / at the end):")
        container_output_dir = input()
        print("Output directory in container saved!")
    if selection == 2:
        print("Enter the new Output directory in host (remeber adding the / at the end):")
        host_output_dir = input()
        print("Output directory in host saved!")

print("Enter the file name: ")
img_file_name = str(input())


print("Start copying the file:\n {0}{1}\ninto:\n {2}? (y/n)".format(container_output_dir,
                                                           img_file_name,
                                                           host_output_dir))

selection = str(input())

if selection in ['Y', 'y']:
    command = 'docker cp {0}:{1}{2} "{3}"'.format(configuration["container-settings"]["container-id"],
                                            container_output_dir,
                                            img_file_name,
                                            host_output_dir)

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