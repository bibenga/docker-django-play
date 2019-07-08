FROM node:12

RUN apt-get update \
    && apt-get install -y apt-utils \
    && apt-get upgrade -y \
    && apt-get install -y \
        supervisor nginx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY supervisor.conf supervisor.conf
COPY nginx.conf nginx.conf
COPY run.sh run.sh

COPY public public
COPY src src

RUN npm run build

EXPOSE 8000

CMD ["/bin/bash", "/opt/app/run.sh"]
