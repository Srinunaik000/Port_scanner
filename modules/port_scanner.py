import socket
import threading

# Function to perform port scanning and determine port status
def port_scan(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ipaddress, port))

        if result == 0:
            print(f"[+] Port {port} is Open")
        elif result == 111:  # Connection refused
            print(f"[-] Port {port} is Closed")
        elif result == 11:  # Host unreachable
            print(f"[?] Port {port} is Filtered (Host unreachable)")

    except socket.timeout:
        print(f"[?] Port {port} is Filtered (timeout)")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")
    finally:
        sock.close()

# Function to scan ports in a thread
def threaded_scan(ipaddress, port):
    thread = threading.Thread(target=port_scan, args=(ipaddress, port))
    thread.start()

# Main function to handle port scanning logic
def main(target, ports):
    ipaddress = socket.gethostbyname(target)  # Convert domain to IP
    print(f'Scanning {ipaddress} for ports: {ports}')

    # Parse port range input
    port_range = ports.split('-')
    start_port = int(port_range[0])
    end_port = int(port_range[1]) if len(port_range) > 1 else start_port

    for port in range(start_port, end_port + 1):
        threaded_scan(ipaddress, port)
