FROM python:3.11.4-alpine3.18

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

RUN apk update && \
    apk add --virtual build-deps libffi-dev gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk add bash

RUN python3 -m pip install psycopg2

RUN python3 -m pip install -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT ["/app/start-server.sh"]

