import socket
import sys
import subprocess

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=1):
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def check_process(name):
    try:
        # Check if process exists using pgrep
        subprocess.check_output(["pgrep", "-f", name])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Service definition: (Display Name, Port, Process Name Pattern)
    services = [
        ("Nginx", 443, "nginx: master process"),
        ("AdGuard Home", 13080, "AdGuardHome"),
        ("DNS (UDP/TCP)", 53, "AdGuardHome"),
        # Add other services as needed
    ]

    results = []
    for name, port, proc_pattern in services:
        port_ok = check_port("127.0.0.1", port)
        proc_ok = check_process(proc_pattern)
        
        status = "OK" if (port_ok and proc_ok) else "FAILED"
        results.append(f"{name:<15} : {status} (Port:{port}, Proc:{'R' if proc_ok else 'D'})")

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
