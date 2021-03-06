FROM python:3.6
USER root

ENV APP_ROOT /webapp
WORKDIR $APP_ROOT

COPY . $APP_ROOT

RUN apt-get update && apt-get install -y unzip \
    # SQLite
    sqlite3 libsqlite3-dev


# pipインストール(最新版)
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python get-pip.py

RUN pip install pipenv
# RUN pipenv lock -r > requirements.txt
# RUN pip install -r requirements.txt
# RUN pip install webdriver-manager

ENTRYPOINT  ["/bin/sh", "-c", "while :; do sleep 10; done"]
