# Use Python 3.11 slim image
FROM python:3.11-slim-buster

# Environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set up the working directory
RUN mkdir /app
WORKDIR /app

# Install dependencies for Selenium and Chromium
RUN apt-get update && \
    apt-get install -y wget unzip curl gnupg && \
    apt-get install -y chromium chromium-driver

# Set Chrome and ChromeDriver paths as environment variables
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install alembic

# Copy application files, including main.py
COPY . .

# Ensure the entrypoint script is executable
RUN chmod +x /app/docker-entrypoint.sh

# Set entrypoint to run the entrypoint script
ENTRYPOINT ["/app/docker-entrypoint.sh"]
