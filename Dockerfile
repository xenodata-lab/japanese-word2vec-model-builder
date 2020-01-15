FROM python:3.6

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y \
    nano \
    less \
    wget \
    git \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN mkdir -p /app
WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt

CMD bash

