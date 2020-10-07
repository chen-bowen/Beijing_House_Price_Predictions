#!/usr/bin/env bash
export IS_DEBUG=${DEBUG:-false}
if [[ -z "${PORT}" ]]; then
    PORT=5000
else
    PORT="${PORT}"
fi

exec gunicorn --bind 0.0.0.0:$PORT --access-logfile - --error-logfile - run:application