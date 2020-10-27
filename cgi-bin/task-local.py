#!/usr/bin/python3
import cgi
import subprocess as sp
print("content-type: text/plain")
print()

form = cgi.FieldStorage()
cmd = form.getvalue("x")
server = form.getvalue("server")
username = form.getvalue("username")
password = form.getvalue("password")

output = sp.getoutput("sudo {}".format(cmd))


print(output)
