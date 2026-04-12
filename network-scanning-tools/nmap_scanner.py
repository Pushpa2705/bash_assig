import subprocess
import sys

def check_nmap():
    try:
        subprocess.run(["nmap", "--version"], capture_output=True)
        return True
    except:
        return False

def run_scan(target, option):
    command = ["nmap"]

    if option == "1":
        command += ["-sn"]              # Host Discovery
    elif option == "2":
        command += ["-p", "1-1000"]     # Port Scan
    elif option == "3":
        command += ["-sV"]              # Service Version Detection
    elif option == "4":
        command += ["-O"]               # OS Detection
        command.append(target)

    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def main():
    if not check_nmap():
        print("Nmap is not installed")
        sys.exit(1)

    if len(sys.argv) < 3:
        print("Usage: python nmap_scanner.py <target> <option> [output_file]")
        print("Options: 1=Host Discovery, 2=Port Scan, 3=Service Version, 4=OS Detection")
        sys.exit(1)

    target = sys.argv[1]
    choice = sys.argv[2]

    print("=== Nmap Scanner ===")
    print(f"Target: {target}, Option: {choice}")
    print("\nScanning...\n")

    output = run_scan(target, choice)
    print(output)

    # Optional file save
    if len(sys.argv) > 3:
        filename = sys.argv[3]
        with open(filename, "w") as f:
            f.write(output)
        print(f"Saved to {filename}")
        if __name__ == "__main__":
            main()
