#!/bin/bash

echo "USER REPORT"

echo "All users:"
cut -d: -f1 /etc/passwd

echo "Currently logged users:"
who

echo "Users with UID 0:"
awk -F: '$3==0 {print $1}' /etc/passwd

echo "Users without password:"
sudo awk -F: '($2==""){print $1}' /etc/shadow 2>/dev/null
