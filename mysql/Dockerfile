FROM mysql

ENV MYSQL_ROOT_PASSWORD youdonthavetoknow
ENV MYSQL_HOST localhost

EXPOSE 3306

ADD ./init.sql /docker-entrypoint-initdb.d
     
