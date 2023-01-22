FROM ubuntu:20.04

ENV DOCKER_CHANNEL=stable 
ENV DOCKER_VERSION=20.10.9 
ENV DOCKER_COMPOSE_VERSION=1.29.2 
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y ca-certificates curl gnupg lsb-release wget curl iptables supervisor
RUN apt update
RUN apt -y install python3-pip
RUN apt -y install git
RUN apt -y install vim
RUN apt install -y python3-tk
RUN pip3 install gunicorn
RUN pip3 install flask
RUN pip3 install python-dotenv
RUN pip3 install requests
RUN pip3 install Flask-Session
RUN pip3 install cryptography
RUN pip3 install mysql-connector-python

CMD ["tail","-f","/dev/null"]