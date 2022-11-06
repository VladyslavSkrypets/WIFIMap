FROM python:3.10-slim-buster
ADD . /service

COPY requirements.txt requirements.txt
WORKDIR /service

RUN pip install --upgrade setuptools pip

RUN pip install -r requirements.txt

