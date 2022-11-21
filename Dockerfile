FROM python:3.9.15-slim
COPY ./requirements.txt /requirements.txt
RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install -r /requirements.txt