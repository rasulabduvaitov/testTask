#!/bin/bash
# docker-entrypoint.sh

# Run Alembic migrations
alembic upgrade head

# Execute main.py
exec python main.py
