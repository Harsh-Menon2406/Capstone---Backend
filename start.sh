#!/bin/bash
if [ ! -f "/opt/render/project/src/project_database.db" ]; then
    echo "Database file not found, creating..."
    python /opt/render/project/src/database_setup.py
fi
gunicorn -w 4 -b 0.0.0.0:10000 Backend_api:app
