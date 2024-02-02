FROM --platform=$TARGETPLATFORM python:3.9-buster AS builder

WORKDIR /project_celery

COPY requirements.txt /project_celery
RUN  apt-get update && \
     apt-get install -y vim && \
     pip3 install -r requirements.txt


COPY ./app /project_celery/app/app