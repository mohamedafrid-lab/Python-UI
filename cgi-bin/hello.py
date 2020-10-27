#! /usr/bin/python3
print("content-type: text/plain")
print()

import textwrap
import subprocess
import cgi

form = cgi.FieldStorage()
server = form.getvalue("server")
username = form.getvalue("username")
password = form.getvalue("password")


'''
test=subprocess.getoutput("sshpass -p{} ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no  {}@{} yum install sress-ng -y".format(password,username,server) )

print(textwrap.fill(test))
'''
state = subprocess.getstatusoutput("ping -c 2 {}".format(server))
status = state[0]


if status == 0:

    subprocess.getoutput("sshpass -p{} ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} sudo rm -rf /tmp/stress-setup.sh &> /dev/null".format(password,username,server) )

    subprocess.getoutput("sshpass -p{} scp -p -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR stress-setup.sh {}@{}:/tmp/stress-setup.sh  &> /dev/null".format(password,username,server))

    subprocess.getoutput("sshpass -p{} scp -p -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR cpu-stress.sh {}@{}:/tmp/cpu-stress.sh  &> /dev/null".format(password,username,server))

    subprocess.getoutput("sshpass -p{} scp -p -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR memory-stress.sh {}@{}:/tmp/memory-stress.sh  &> /dev/null".format(password,username,server))

    test=subprocess.getoutput("sshpass -p{} ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR {}@{} cd /tmp; sudo bash stress-setup.sh -y 2> /dev/null".format(password,username,server))

    print(test)

else:

    print("Server is not reachable")






