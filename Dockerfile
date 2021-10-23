FROM python:3.8.8

WORKDIR /usr/src

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src
