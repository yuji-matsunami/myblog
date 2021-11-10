# Python3イメージを元にする
FROM python:3
# バイナリレイヤ間で標準出力とエラー出力を制御
ENV PYTHONUNBUFFERD 1

RUN mkdir /code
RUN apt-get update
# 日本語対応させる
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
WORKDIR /code
RUN pip install --upgrade pip
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
ADD . /code/