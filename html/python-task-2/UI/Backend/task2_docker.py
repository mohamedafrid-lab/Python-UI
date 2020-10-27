#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
osname = form.getvalue("x")
osimage = form.getvalue("i")
cmd = "sudo docker start {0}".format(osname)
output1 = sp.getstatusoutput(cmd)
status1 = output1[0]
out1 = output1[1]
if status1 == 0:
	print("OS name {} has been started".format(osname))
else:
	print("Error occured during starting is {}".format(out1))
