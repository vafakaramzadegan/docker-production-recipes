#!/bin/sh

exec systemctl start supervisor &
exec gunicorn --workers 8 --reload --log-level=DEBUG --bind 0.0.0.0:5000 app:app