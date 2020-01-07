#!/usr/bin/env bash

source run.sh &
sleep 2
curl 'http://127.0.0.1:5000/login' -d 'email=benek@sad.ss&password=benek2000'
sleep 3
curl 'http://127.0.0.1:5000/logout'
sleep 3
kill `ps aux | grep -i flask | grep python | sed -E 's/([a-z]+ *)([0-9]+)(.*)/\2/g'`