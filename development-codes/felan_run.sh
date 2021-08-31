#!/bin/bash

file=$1

while IFS=$' \t\n\r' read -r cmd; do
     python3.6 nums.py "$cmd"
done < "$1"



