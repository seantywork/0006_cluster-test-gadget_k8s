FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d

COPY static /var/www/UC/static

COPY media /var/www/UC/media

EXPOSE 5005


