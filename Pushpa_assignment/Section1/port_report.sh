#!/bin/bash
if [ -z "$1" ]; then
echo "Usage: $0 <IP>"
exit 1
fi
IP=$1
PORT=(21 22 80 443 3306)
for port in "${PORT[@]}"; do 
nc -z -w1 $IP $port
if [ $ -eq 0 ]; then
echo "Port $port OPEN"
else
echo "Port $port CLOSED"
fi
done
