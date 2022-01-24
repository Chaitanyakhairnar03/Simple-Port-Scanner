#!/usr/bin/env python3

import sys
import datetime
import socket
count = 0

print("-" *50)
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate host to ip
else: 
    print("[-] Invalid Syntax")
    print("[-] syntax: python3 port_scanner <IP address/hostname>")
    print("-" * 50)
    sys.exit()

print("[+] Scanning targetL: "+ target)
print("[+] Time started: "+str(datetime.datetime.now()))
print("-" * 50)

try:
    no_ports = int(input("[+] How many ports would you like to scan? "))
    print("[+] Scanning for first {} ports \n".format(no_ports))
    for port in range(1,no_ports):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target,port))
        if result == 0:
            print("[+] Port {} is open ".format(port))
            count += 1
        s.close()
    print("-" * 50)
    print("[+] Found {} open ports".format(count))
    print("[+] Program closing Time "+ str(datetime.datetime.now()))
    print("-" * 50)
except KeyboardInterrupt:
    print("[-] Interrupted by keyboard.")
    print("[-] Exiting program...")
    sys.exit()
except socket.gaierror:
    print("[-] Hostname couldn't be resolved.")
    print("[-] Exiting program...")
    sys.exit()
except socket.error:
    print("[-] Couldn't able to connect to the {}".format(target))
    print("[-] Exiting program...")
    sys.exit()