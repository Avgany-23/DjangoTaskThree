FROM python:3.12.0-alpine

LABEL author='author_main'

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update \
    gcc \
    musl-dev \
    python3-dev \
    make \
    && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app