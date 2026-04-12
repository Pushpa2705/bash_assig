import subprocess
import platform
import re
import sys

def ping_host(host):
    # Use -n for Windows, -c for Linux/macOS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout

        # Check reachability
        if "unreachable" in output.lower():
            status = "Unreachable"
        else:
            status = "Reachable"

        # Extract average time (Windows format)
        avg_time = "N/A"
        match = re.search(r"Average = (\d+)ms", output)
        if match:
            avg_time = match.group(1) + " ms"

        return status, avg_time

    except Exception as e:
        return "Error", str(e)

def main():
    if len(sys.argv) < 2:
        print("Usage: python ping_scanner.py <host1> <host2> ...")
        sys.exit(1)

    hosts = sys.argv[1:]
    for host in hosts:
        status, avg = ping_host(host)
        print(f"{host} -> {status} | Avg: {avg}")

if __name__ == "__main__":
    main()