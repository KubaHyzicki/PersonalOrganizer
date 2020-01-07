#!/usr/bin/env bash

source .config

python3 -m flask run --host=${HOST} --port=${PORT}
