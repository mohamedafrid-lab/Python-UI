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
test = form.getvalue("test")
worker_num = form.getvalue("worker_num")
timeout = form.getvalue("timeout")
CPU = form.getvalue("CPU")
io = form.getvalue("io")
Memory = form.getvalue("Memory")




if CPU == 'CPU':
    
    output = sp.getoutput("sshpass -p{} ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} sudo stress --cpu {} --timeout {}".format(password,username,server,worker_num,timeout))

    cpu_output = sp.getoutput("sshpass -p{} ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} sudo 'bash /tmp/cpu-stress.sh > /tmp/cpu-stress.txt; cat /tmp/cpu-stress.txt'".format(password,username,server))

    print(cpu_output) 

if Memory == 'Memory':

    mmy_output = sp.getoutput("sshpass -p{} ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} 'sudo stress --vm {} --timeout {}'".format(password,username,server,worker_num,timeout))

    mmy_output = sp.getoutput("sshpass -p{} ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} sudo 'bash /tmp/memory-stress.sh > /tmp/memory-stress.txt; cat /tmp/memory-stress.txt'".format(password,username,server))

    print(mmy_output) 


if io == 'io':

    io_output = sp.getoutput("sshpass -p{} ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} sudo stress --io {} --timeout {}".format(password,username,server,worker_num,timeout))

    io_output = sp.getoutput("sshpass -p{} ssh -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=ERROR  {}@{} iostat".format(password,username,server))

    print(io_output) 


