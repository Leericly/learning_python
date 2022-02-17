"""
Port Scanning App
From Infosec's Youtube video posted on 27Aug21
https://www.youtube.com/watch?v=t9EX2RAUoTU
"""

import socket
import sys
from datetime import datetime

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("Please wait, scanning remote host", remoteServerIP)
print("_" * 60)

t1 = datetime.now()

try:
    for port in range(1, 5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(f"Port {port}:         Open")
        else:
            print(f"Port {port}:         Closed")
            end = timeit.timeit()
        sock.close()

except KeyboardInterrupt:
    print("Hostname could not be resolved. Exiting")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()

t2 = datetime.now()

total = t2 - t1
print("Scanning Completed in: ", total)
