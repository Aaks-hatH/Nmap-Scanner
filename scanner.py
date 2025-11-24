import socket
import sys
from datetime import datetime

'''
Made By Aakshat Hariharan
for Ethical use only
v 1.0
'''
print("-" * 50)
print("PYTHON PORT SCANNER (TCP)")
print("-" * 50)

# target
try:
    target = input("Enter target IP (e.g., 127.0.0.1): ")
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()

print(f"Scanning Target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1) # Fast timeout
        
        #should say 0 for open ports
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\n[!] Exiting Program.")
    sys.exit()
except socket.gaierror:
    print("\n[!] Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\n[!] Could not connect to server.")
    sys.exit()

print("-" * 50)
print("Scan completed.")
