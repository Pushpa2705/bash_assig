#!/bin/bash

while true
do
echo "1.Create File"
echo "2.Delete File"
echo "3.List Files"
echo "4.Create Directory"
echo "5.Exit"
read -p "Enter choice: " ch

case $ch in
1) read -p "File name: " f; touch $f;;
2) read -p "File name: " f; rm -i $f;;
3) ls;;
4) read -p "Dir name: " d; mkdir $d;;
5) exit;;
*) echo "Invalid";;
esac
done
