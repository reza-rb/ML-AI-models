#!/bin/bash

# Usage: ./organize.sh /path/to/folder

if [ "$#" -ne 1 ]; then
  echo "Usage: ./organize.sh <folder_path>"
  exit 1
fi

python3 organize.py "$1"

