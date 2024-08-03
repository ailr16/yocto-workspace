#!/bin/sh

sudo add-apt-repository ppa:deadsnakes/ppa --yes

sudo apt install -y software-properties-common gawk wget  git diffstat unzip texinfo gcc build-essential \
               chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils \
               iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev python3-subunit \
               mesa-common-dev zstd liblz4-tool file locales libacl1 nano screen tree

locale-gen en_US.UTF-8

mkdir /home/$USER/yocto
cd /home/$USER/yocto
git clone git://git.yoctoproject.org/poky -b nanbield
git clone git://git.openembedded.org/meta-openembedded -b nanbield
git clone git://git.yoctoproject.org/meta-raspberrypi -b nanbieldg