#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
status = subprocess.getoutput("sudo docker ps")
print(status)
