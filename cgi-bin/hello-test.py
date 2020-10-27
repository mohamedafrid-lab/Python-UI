#! /usr/bin/python3
print("content-type: text/html")
print()


import subprocess
import cgi
'''
form = cgi.FieldStorage()
server = form.getvalue("server")
username = form.getvalue("username")
password = form.getvalue("password")
'''

server = "13.127.210.198"
password = "redhat"
username = "root"


subprocess.getoutput("sshpass -p{} ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} sudo rm -rf /tmp/stress-setup.sh &> /dev/null".format(password,username,server) )

subprocess.getoutput("sshpass -p{} scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR stress-setup.sh {}@{}:/tmp/stress-setup.sh  &> /dev/null".format(password,username,server))

test=subprocess.getoutput("sshpass -p{} ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR {}@{} cd /tmp; sudo bash stress-setup.sh 2> /dev/null".format(password,username,server))

print(test)



