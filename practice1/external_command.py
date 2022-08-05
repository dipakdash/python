#!/usr/bin/python3

import subprocess
import re

def get_interface_ip():
    command = "ip addr show dev eth1"
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

    regex = 'inet\s+(.*)\/'
    p = re.compile(regex)
    ip = p.findall(result)
    return ' '.join(ip)

if __name__ == "__main__":
    print(f'IP address of the system is: { get_interface_ip() }')
