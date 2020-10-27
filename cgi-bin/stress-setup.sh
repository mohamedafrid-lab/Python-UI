#! /bin/bash

loc=`yum info stress &>  /dev/null;  echo $?`
if [ $loc -eq 0 ]
then
	echo "All is set to go"
else
	cd /tmp
	wget ftp://fr2.rpmfind.net/linux/dag/redhat/el7/en/x86_64/dag/RPMS/stress-1.0.2-1.el7.rf.x86_64.rpm
	yum localinstall stress-1.0.2-1.el7.rf.x86_64.rpm
	yum install systat -y
	sudo service sysstat restart
fi
