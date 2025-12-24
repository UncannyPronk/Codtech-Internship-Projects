import socket

def run():
    target = input("Enter target IP or hostname: ").strip()
    ports = [21, 22, 80, 443]

    print("\nStarting port scan...\n")

    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is CLOSED")

            sock.close()
        except Exception:
            print(f"[!] Could not scan port {port}")

    print("\nPort scan completed.")
