#!/bin/bash

echo "System Information"
echo "------------------"
echo "Hostname: $(hostname)"
echo "OS: $(uname -o)"
echo "Kernel: $(uname -r)"
echo "Uptime: $(uptime -p)"
echo "CPU: $(lscpu | grep 'Model name' | cut -d ':' -f2)"
echo "Memory:"
free -h
echo "Disk:"
df -h
