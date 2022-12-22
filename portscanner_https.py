from socket import timeout
import socket
import os
from sys import platform, exit

print("""\033[31m    ____             __                                              
   / __ \____  _____/ /_   ______________ _____  ____  ___  _____    
  / /_/ / __ \/ ___/ __/  / ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/    
 / ____/ /_/ / /  / /_   (__  ) /__/ /_/ / / / / / / /  __/ /        
/_/    \____/_/   \__/  /____/\___/\__,_/_/ /_/_/ /_/\___/_/         
                                                                     """)  # hacker logo
print("\033[0m")

if platform == "win32":
    import ctypes

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)  # ANSI for windows console

address = input("IP address: ")
try:
    socket.socket().connect((address, 80))
except socket.gaierror:
    print("\033[34mInvalid IP address. Do you use IP address or domain? (use IP address). \033[0m")
    exit()

if os.path.exists(f"{address}.txt"):
    with open(f"{address}.txt", "w") as swecan:  # if file exits - clear text
        swecan.close()

with open(f"{address}.txt", "a") as port_file:
    for port in range(1, 65535 + 1):
        try:
            sock = socket.socket()
            sock.settimeout(0.01)
            sock.connect((address, port))
            print(f"\033[32m[+] {port} is open.")
            port_file.write(str(port))
            port_file.write("\n")
        except ConnectionRefusedError:
            print(f"\033[31m[-] {port} is closed.")
        except timeout:
            print(f"\033[31m[-] {port} is closed(timeout).")
            continue
        except OSError:
            print(f"\033[31m[-] {port} is closed(perhaps Firewall).")
    else:
        print("\n\n\n\n\n\n\n\n")
        print(f"\033[0mThe result was written to:\033[0m \033[37m\033[7m{address}.txt\033[0m")
