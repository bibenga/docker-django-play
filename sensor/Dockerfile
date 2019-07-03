FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y apt-utils \
    && apt-get upgrade -y \
    && apt-get install -y \
        python3.7 python3.7-dev python3-pip python3-venv python3-setuptools python3-wheel \
        openssl libssl-dev libpcre3-dev git \
        postgresql-client \
        libtiff5-dev libjpeg-dev libzip-dev zlib1g-dev libffi-dev libfontconfig-dev \
        libxml2-dev libxslt1-dev \
        libgdal-dev libgeos-dev libproj-dev \
        git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -U pip setuptools \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY manage.py manage.py
COPY uwsgi.ini uwsgi.ini
COPY run.sh run.sh

ENV DJANGO_SETTINGS_MODULE sensor.settings.prod

COPY sensor sensor

EXPOSE 8000

CMD ["/bin/bash", "/opt/app/run.sh"]
