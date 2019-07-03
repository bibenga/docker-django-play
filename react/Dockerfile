FROM node:12

WORKDIR /opt/app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY run.sh run.sh
COPY public public
COPY src src

RUN npm run build

EXPOSE 3000

CMD ["/bin/bash", "/opt/app/run.sh"]
