FROM python:3.10.6
ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
