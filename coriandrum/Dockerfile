FROM ubuntu:14.04

# System requirements installation

RUN apt-get update && \
	apt-get install -y libxml2-dev libxslt1-dev python3-dev python3-setuptools python3.4 build-essential python3-pip nginx libpq-dev mysql-client libmysqlclient-dev curl && \
	apt-get --assume-yes install -f libjpeg-dev zlib1g-dev && \
	ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib && \
	ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib && \
	ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

# Encoding fix for correct UTF handling in python packages

RUN sudo locale-gen "en_US.UTF-8"
ENV LC_CTYPE "en_US.UTF-8"
ENV LC_NUMERIC "en_US.UTF-8"
ENV LC_TIME "en_US.UTF-8"
ENV LC_COLLATE "en_US.UTF-8"
ENV LC_MONETARY "en_US.UTF-8"
ENV LC_MESSAGES "en_US.UTF-8"
ENV LC_PAPER "en_US.UTF-8"
ENV LC_NAME "en_US.UTF-8"
ENV LC_ADDRESS "en_US.UTF-8"
ENV LC_TELEPHONE "en_US.UTF-8"
ENV LC_MEASUREMENT "en_US.UTF-8"
ENV LC_IDENTIFICATION "en_US.UTF-8"
RUN locale

# Python packages installation

COPY requirements.txt /opt/app/requirements.txt

RUN pip3 install uwsgi
RUN pip3 install -r /opt/app/requirements.txt

# Copying application code into container

COPY . /opt/app

VOLUME ["/opt/media"]

WORKDIR /opt/app

# Creating secret application code if not exists

RUN if [ ! -f secret_key.txt ]; then openssl rand -base64 32 > secret_key.txt; fi

CMD python3 manage.py collectstatic --noinput

CMD python3 manage.py migrate --noinput && uwsgi --ini=uwsgi.ini

EXPOSE 80
