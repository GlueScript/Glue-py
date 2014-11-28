FROM ubuntu:latest
MAINTAINER Tim Rodger

RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

RUN apt-get update -qq && apt-get install -y tar \
    git \
    curl \
    dialog \
    net-tools
    build-essential \
    python \
    python-dev \
    python-distribute \
    python-pip
