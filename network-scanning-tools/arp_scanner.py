import subprocess
import re
import sys

def get_arp_table():
    result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    return result.stdout

def parse_arp(output):
    pattern = r"(\d+\.\d+\.\d+\.\d+)[\s\-]+([a-fA-F0-9:-]{17})"
    return re.findall(pattern, output)

def main():
    print("=== ARP Scanner ===")

    output = get_arp_table()
    entries = parse_arp(output)

    print("\nIP Address\t\tMAC Address")
    print("----------------------------------------")
    for ip, mac in entries:
        print(ip, "\t", mac)

    print("\nTotal entries:", len(entries))

    # If user passed a filename argument, save results
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, "w") as f:
            for ip, mac in entries:
                f.write(f"{ip} {mac}\n")
        print(f"Saved to {filename}")

if __name__ == "__main__":
    main()