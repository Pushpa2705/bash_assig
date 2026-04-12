#!/bin/bash

read -p "Enter source directory: " src
read -p "Enter backup directory: " dest

timestamp=$(date +%Y%m%d_%H%M%S)

mkdir -p $dest
cp -r $src $dest/backup_$timestamp

echo "Backup completed: backup_$timestamp"
