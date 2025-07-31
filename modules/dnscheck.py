import socket

import socket

def is_port_open(host, port):
    try:
        # First test DNS resolution
        ip = socket.gethostbyname(host)
        
        # Then try socket connection
        with socket.create_connection((ip, port), timeout=5):
            return True
    except Exception as e:
        return False


print(is_port_open("google.com", 21))  # → True
print(is_port_open("sibervatxan.org", 6661))   # → False
