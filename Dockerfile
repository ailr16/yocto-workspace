FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y tzdata && \
    apt update && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa --yes && \
    apt install -y python3.8 && \
    rm /usr/bin/python3 && \
    ln -s /usr/bin/python3.8 /usr/bin/python3 && \
    alias python3='/usr/bin/python3.8' && \
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
    git clone git://git.yoctoproject.org/poky

CMD /bin/bash