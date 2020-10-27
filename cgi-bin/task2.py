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

output = sp.getoutput("sshpass -p{} ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} sudo {}".format(cmd))


print(output)
