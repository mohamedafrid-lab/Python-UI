#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
image = subprocess.getoutput("sudo docker images")
print(image)
