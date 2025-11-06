#!/usr/bin/env bash
# shellcheck disable=SC2164
cd /data/recruitment/src/recruitment
uvicorn recruitment.asgi:application --host 0.0.0.0 --port 39979

