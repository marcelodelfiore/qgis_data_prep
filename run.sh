#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./run.sh <filename (without .xlsx)>"
  exit 1
fi

python3 script.py "$1"
