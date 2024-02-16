FROM ubuntu:22.04

RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone && \
    apt-get update && \
    apt update && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa --yes && \
    apt install -y gawk && \
    apt install -y wget  && \
    apt install -y git  && \
    apt install -y diffstat  && \
    apt install -y unzip  && \
    apt install -y texinfo && \
    apt install -y gcc  && \
    apt install -y build-essential && \
    apt install -y chrpath && \
    apt install -y socat && \
    apt install -y cpio && \
    apt install -y python3 && \
    apt install -y python3-pip && \
    apt install -y python3-pexpect && \
    apt install -y xz-utils && \
    apt install -y debianutils && \
    apt install -y iputils-ping && \
    apt install -y python3-git && \
    apt install -y python3-jinja2 && \
    apt install -y libegl1-mesa && \
    apt install -y libsdl1.2-dev && \
    apt install -y python3-subunit && \
    apt install -y mesa-common-dev && \
    apt install -y zstd && \
    apt install -y liblz4-tool && \
    apt install -y file && \
    apt install -y locales && \
    apt install -y libacl1 && \
    apt install -y nano && \
    locale-gen en_US.UTF-8 && \
    adduser --system --group yocto-user && \
    usermod -aG sudo yocto-user

USER yocto-user

RUN cd /home/yocto-user/ && \
    mkdir yocto && \
    cd yocto && \
    git clone git://git.yoctoproject.org/poky

CMD cd /home/yocto-user/yocto; \
    /bin/bash