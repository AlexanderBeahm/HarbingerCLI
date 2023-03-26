# syntax=docker/dockerfile:1

FROM python:3.9.5-slim-buster

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

USER app_user

COPY . .

CMD [ "python3", "-m" , "harbinger"]
