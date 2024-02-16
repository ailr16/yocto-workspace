# Ubuntu for Yocto/Poky (Docker image)
Here are files related to building a Yocto image.

View on Docker Hub:  
https://hub.docker.com/repository/docker/ailr16/ubuntu-for-yocto/general

I've tested on Windows 11 Pro

<mark>The container provides the environment to build the image using:
- <mark>Ubuntu 22.04
- <mark>Poky (tested with nanbield branches)


## Building docker image
For any customization here is the Dockerfile.
- After making changes in Dockefile, inside the repo directory:
    ```
    docker build -t ubuntu-for-yocto . 
    ```

## Run the container
- Run my latest version in interactive mode:
    ```
    docker run -it ailr16/ubuntu-for-yocto:latest
    ```

- Or run the image with the nanbield branch (just for avoid errors due to no switching to this branch):
    ```
    docker run -it ailr16/ubuntu-for-yocto:nanbield
    ```

## Get the output files
The working directory is:
    ```
    /home/yocto-user/yocto/
    ```
- Copy output files with:
    ```
    docker cp <containerId>:/home/yocto-user/yocto/... <path_in_host>
    ```