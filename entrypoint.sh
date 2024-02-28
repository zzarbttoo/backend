#!/bin/bash

if [ "$PYTHON_PROFILES_ACTIVE" == "dev" ]; then
    ENV_FILE="backend/app/config/dev.env"
elif [ "$PYTHON_PROFILES_ACTIVE" == "ops" ]; then
    ENV_FILE="backend/app/config/ops.env"
else
    ENV_FILE="backend/app/config/local.env"
fi

exec python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --env-file "$ENV_FILE"
