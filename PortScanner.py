from socket import socket, AF_INET, SOCK_STREAM

print("TCP Port Scanner.\nEnter the target IP address and the ports you want to scan (comma-separated).")
target_ip = input("Target IP: ").strip()
ports = input("Ports: ")
port_list = [int(port.strip()) for port in ports.split(",")]
print(f"\nScanning {target_ip}...\n")

for port in port_list:
    with socket(AF_INET, SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect((target_ip, port))
            state = "open"
        except ConnectionRefusedError:
            state = "refused"
        except TimeoutError:
            state = "timeout"
    print(f"Port {port}: {state}")