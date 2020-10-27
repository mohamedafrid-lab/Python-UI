#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
version = subprocess.getoutput("sudo docker --version")
print(version)
