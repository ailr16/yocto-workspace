# Environment for building Yocto images
## Using a Docker container

Building the image takes a long. I've created an image for the different platforms, Raspberry Pi and Jetson Nano, cloning the repos for the minimal required setup and saving around 5 minutes. The images details:
- Raspberry Pi:
    - Ubuntu 22.04
    - Uses _yocto_user_ as owner for avoiding problems with the root user
    - Clones __Poky__ _nanbield_ branch
    - Clones __meta-openembedded__ _nanbield_ branch
    - Clones __meta-raspberrypi__ _nanbield_ branch
    - The working directory is: /home/yocto-user/yocto
    - DockerHub: ___WIP___

- Nvidia Jetson Nano:
    - Ubuntu 22.04
    - Uses _yocto_user_ as owner for avoiding problems with the root user
    - Clones __Poky__ _kirkstone_ branch
    - Clones __openembedded-core__ _kirkstone_ branch
    - Clones __meta-tegra__ _kirkstone_ branch
    - The working directory is: /home/yocto-user/yocto
    - DockerHub: ___WIP___

### Building the image
Go to the platform directory and run:
```
docker build -t <image_name> .
```

### Run the container
```
docker run -it <image_name>:latest
```

### Run an existing container
```
docker start CONTAINER_ID
docker exec -it CONTAINER_ID /bin/bash
```

### Get the output files
```
docker cp <containerId>:/home/yocto-user/yocto/... <path_in_host>
```


## Using a Virtual Machine - WIP


# Deprecated. Needs a review.

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

## Install dependencies
Run *install_dependencies.sh*  
**NOTE1: This will prompt asking for the sudo password**  
**NOTE2: This will create the workspace directory in /home/$USER/yocto**
```
./Linux/install_dependencies.sh
```

## For VMs: Create shared filesystem between Host-Guest
Run *guestvm/mount_sharedfs.sh* in the guest
```
./Linux/guestvm/mount_sharedfs.sh
```
This will create a directory in */mnt/yocto_output* and mount the filesystem there.
Copy the output files to that dir to share with the Host.

NOTE: The next image show the configuration for filesystem in virt-manager:
![fs example](/Linux/docs/img/fs_pass.png)