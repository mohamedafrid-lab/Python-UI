#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
osname = form.getvalue("x")
osimage = form.getvalue("i")
output = sp.getoutput("sudo podman inspect {}".format(osname))
print(output)
