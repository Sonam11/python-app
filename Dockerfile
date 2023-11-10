FROM python:3.6-slim-stretch

COPY requirements.txt /

WORKDIR /

RUN pip install -r ./requirements.txt --no-cache-dir

COPY app/ /app/

WORKDIR /app

ENV FLASK_APP=app.py

CMD flask run -h 0.0.0.0 -p 5000 --with-threads
