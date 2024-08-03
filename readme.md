# Linux

## Install dependencies
Run *install_dependencies.sh*  
**NOTE1: This will prompt asking for the sudo password**  
**NOTE2: This will crete the workspace directory in /home/$USER/yocto**
```
./Linux/install_dependencies.sh
```

# Windows

## Ubuntu for Yocto/Poky (Docker image)
Here are files related to building a Yocto image.

View on Docker Hub:  
https://hub.docker.com/repository/docker/ailr16/ubuntu-for-yocto/general

Tested on Windows 11 Pro

<mark>The container provides the environment to build the image using:
- <mark>Ubuntu 22.04
- <mark>Poky (tested with nanbield branches)


### Building docker image
For any customization here is the Dockerfile.
- After making changes in Dockefile, inside the repo directory:
    ```
    docker build -t ubuntu-for-yocto . 
    ```

### Run the container
- Run my latest version in interactive mode:
    ```
    docker run -it ailr16/ubuntu-for-yocto:latest
    ```

- Or run the image with the nanbield branch (just for avoid errors due to no switching to this branch):
    ```
    docker run -it ailr16/ubuntu-for-yocto:nanbield
    ```
- Run an existing container with:
    ```
    docker start CONTAINER_ID
    docker exec -it CONTAINER_ID /bin/bash
    ```
  

### Get the output files
The working directory is:
    ```
    /home/yocto-user/yocto/
    ```
- Copy output files with:
    ```
    docker cp <containerId>:/home/yocto-user/yocto/... <path_in_host>
    ```
    
### WIP. Emulating with QEMU
	```
	qemu-system-aarch64 -machine virt \
	-cpu cortex-a72 \
	-smp 4 \
	-m 4G \
	-kernel Image.img \
	-append "root=/dev/vda2 rootfstype=ext4 rw panic=0 console=ttyAMA0,115200" \
	-drive format=raw,file=rpilinux-image-raspberrypi4-64.rootfs-20240516061418.wic,if=none,id=hd0,cache=writeback \
	-device virtio-blk,drive=hd0,bootindex=0 \
	-netdev user,id=mynet,hostfwd=tcp::2222-:22 \
	-device virtio-net-pci,netdev=mynet \
	-monitor telnet:127.0.0.1:5555,server,nowait \
	-vga std
	```
