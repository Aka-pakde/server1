#!/bin/bash
if [ -d $HOME/payload ]
then
	rm -rf $HOME/payload
fi
mkdir $HOME/payload
if [ -d $HOME/server ]
then
	echo ''
	echo 'Checking folder directory'
	sleep 2
	echo '[✔] Perfect'
	sleep 2
	echo ''
else
	echo ''
	sleep 2
	echo 'Moving server folder to HOME'
	sleep 2
	mv `pwd` $HOME
	sh setup.sh
	exit
fi
apt-get update
apt-get upgrade
apt-get install unzip -y
apt-get install figlet -y
apt-get install python2 -y
apt-get install php -y
apt-get install openssh -y
apt-get install nmap -y
apt-get install curl -y

rm -rf $PREFIX/bin/server

chmod +x ser.sh

if [ -e $HOME/ser.sh ]
then
	rm $HOME/ser.sh
fi
cp `pwd`/ser.sh $HOME
ln -s $HOME/ser.sh $PREFIX/bin/server
chmod +x serphp.py
if [ -d `pwd`/meta ]
then
	rm -rf `pwd`/meta
fi
mkdir `pwd`/meta
#clear
echo ""
echo ""
echo "just execute [server]"
