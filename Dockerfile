FROM python:3.11-slim-buster

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y wget unzip curl gnupg && \
    apt-get install -y chromium chromium-driver

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install alembic

COPY . .

RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]
