#!/bin/bash
cd "$(dirname "$0")"
exec gunicorn -w 4 app:app --bind 127.0.0.1:5000
