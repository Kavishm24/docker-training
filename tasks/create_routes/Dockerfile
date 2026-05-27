from nginx

RUN apt-get update && apt-get install -y curl


COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./main/index.html /var/www/html/index.html

