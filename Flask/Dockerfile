FROM python:3.10.6-bullseye

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]