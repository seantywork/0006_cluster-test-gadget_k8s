FROM python:3.9

WORKDIR /UC

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt install python3-venv -y \
    && apt install default-libmysqlclient-dev -y \
    && apt install gcc -y \
    && apt install python3-dev -y \
    && apt install libssl-dev -y 

COPY ./requirements.txt /UC/requirements.txt

RUN pip install -r requirements.txt

COPY . /UC

EXPOSE 8000


CMD ["gunicorn","--bind=0.0.0.0:8000","--workers=2","UC.wsgi:application","--access-logfile=-","--error-logfile=-"]


