FROM python:3.13.1

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y build-essential make \
    && pip install -r requirements.txt

COPY . /usr/src/app

CMD [ "make", "m", "up", "r" ]