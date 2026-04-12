#!/bin/bash

read -p "Enter log file: " log

echo "Total lines:"
wc -l $log

echo "Error count:"
grep -i error $log | wc -l

echo "Warning count:"
grep -i warning $log | wc -l

echo "Unique IPs:"
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' $log | sort -u
