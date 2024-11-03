#!/bin/bash
# docker-entrypoint.sh

alembic upgrade head

exec python main.py
