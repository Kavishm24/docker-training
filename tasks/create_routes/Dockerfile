from nginx

RUN apt-get update && apt-get install -y curl

# COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /usr/local/nginx/conf/nginx.conf
COPY ./pages /data/www