<<<<<<< HEAD
Network Scanning Tools

Project Overview

This project implements basic network scanning tools using Python.
The purpose of this project is to understand how devices on a network can be discovered and analyzed using simple scanning techniques.

The tools developed in this project help identify active hosts, display IP and MAC address mappings, and perform basic network scanning operations.

Tools Used

* Python
* Visual Studio Code
* Nmap
* Windows Command Prompt

Project Modules

1. Ping Scanner

The Ping Scanner checks whether a host is reachable on the network.
It sends ICMP requests to a target IP address and verifies if the device responds.

2. ARP Scanner

The ARP Scanner displays the ARP table of the system.
It shows the mapping between IP addresses and MAC addresses of devices connected to the local network.

3. Nmap Scanner

The Nmap Scanner uses the Nmap tool to scan a host and gather information about the network.
It helps identify active hosts and sometimes provides information about the operating system.

Project Files

*ping_scanner.py – Script to perform ping scanning
*arp_scanner.py – Script to display ARP table information
* nmap_scanner.py – Script to perform network scanning using Nmap
*screenshots – Folder containing screenshots of program outputs

How to Run

1. Open the project folder in Visual Studio Code.
2. Open the terminal in VS Code.
3. Run the following commands:

python ping_scanner.py
python arp_scanner.py
python nmap_scanner.py

Output

The output of each program is displayed in the terminal and screenshots are stored in the screenshots folder.

Conclusion

This project demonstrates how Python can be used to perform simple network scanning tasks and helps understand basic concepts of network security and host discovery.
=======

Name:V Pushpa  
Course Work: Bash Scripting Assignment

This repository includes a collection of bash scripts created to demonstrate automation of common Linux system tasks.  
Each script focuses on a different functionality such as system monitoring, file handling, log processing, backup creation, and user reporting.

Q1 – System Information Script
A script designed to fetch and display important system details like memory usage, disk space, and active users.
Q2 – File Management Script
Implements basic file operations including creating, deleting, renaming, and listing files or directories.
Q3 – Log Analysis Script
Processes log files to identify error messages and generate a summary of log statistics.
Q4 – Backup Automation Script
Creates backup copies of specified directories and stores them safely in a backup folder.
Q5 – User Activity Report Script
Generates a report showing user-related information and login details.


Execute the following commands in terminal:
chmod +x *.sh
./q1_system_info.sh
./q2_file_manager.sh
./q3_log_analyzer.sh
./q4_backup.sh
./q5_user_report.sh


All scripts were executed through terminal commands and verified using sample input data.

While completing the assignment, challenges included troubleshooting script errors and understanding various bash commands.
>>>>>>> 1bca48d8e52e8207e0c0b4e4ae34c1d4218bf178
