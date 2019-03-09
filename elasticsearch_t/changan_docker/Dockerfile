# platform env of es monitor
FROM harbor.ainnovation.com/runtime/python:3.6
MAINTAINER LiuQingwei "liuqingwei@chuangxin.com"
ENV REFRESHED_AT 2018-11-22

# work dir.
RUN test -d /root/src || mkdir /root/src
WORKDIR /root/src

COPY requirements.txt requirements.txt

# install python package.
RUN pip install setuptools==40.6.2
RUN pip install -r requirements.txt
