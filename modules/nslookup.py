import os, sys, subprocess


def ip_finder(target):
    command = ['nslookup', target]
    ip = subprocess.run(command, capture_output=True)
    ip = ip.stdout.decode('utf-8')
    ip = ip.split(':');ip = ip[-1];ip = ip.strip()
    return ip
    
