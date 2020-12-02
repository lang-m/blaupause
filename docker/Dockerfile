FROM ubuntu:20.04

RUN apt update -y
RUN apt install -y python3-pip curl
RUN python3 -m pip install --upgrade pip pytest-cov nbval pycodestyle

COPY . /usr/local/discretisedfield/
WORKDIR /usr/local/discretisedfield
RUN python3 -m pip install .
