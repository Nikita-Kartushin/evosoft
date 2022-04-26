FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /evosoft

WORKDIR /evosoft

COPY requirements.txt /evosoft/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /evosoft/