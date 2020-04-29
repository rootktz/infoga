import requests
import os
def clear():
	os.system('clear')
	
def logo():
	print('\033[36m')
	print('''\t#############################''')
	print('''\t#[+]Myanmar Cyber Pirates[+]#''')
	print('''\t#          coded by X-Ray   #''')
	print('''\t#hackertarget api tool      #''')
	print('''\t#############################''')#Don't edit logo
def menu():#main
	print('\033[32m')
	print('1.Dnslookup        5.Whoislookup')
	print('2.Nmap             6.Subnetlookup')
	print('3.Reverseiplookup  7.BannerGrabbing')
	print('4.Tracerout        8.Geoiplookup')
	choice=input("\nPlease choice::")
	if choice=='1':
		dnslookup()
	elif choice=='2':
		nmap()
	elif choice=='3':
		reverseiplookup()
	elif choice=='4':
		tracerout()	
	elif choice=='5':
		whois()
	elif choice=='6':
		subnet()
	elif choice=='7':
		banner()	
	elif choice=='8':
		geoip()
	back()
			
def dnslookup():#dnslookup
	x=input("Enter site::")
	r=requests.get("https://api.hackertarget.com/dnslookup/?q="+str(x))
	print(r.text)
	
def nmap():#nmap
	x=input("Enter site::")
	r=requests.get("https://api.hackertarget.com/nmap/?q="+str(x))
	print(r.text)
	
def reverseiplookup():#reverseip
	x=input("Enter site::")
	r=requests.get("https://api.hackertarget.com/reverseiplookup/?q="+str(x))
	print(r.text)
	
def tracerout():#trace
	x=input("Enter site::")
	r=requests.get("https://api.hackertarget.com/mtr/?q="+str(x))
	print(r.text)	

def whois():#whois
	x=input("Enter site::")
	r=requests.get("https://api.hackertarget.com/whois/?q="+str(x))
	print(r.text)	

def subnet():
	x=input("Enter site::")
	r=requests.get("https://api.hackertarget.com/subnetcalc/?q="+str(x))
	print(r.text)

def banner():
	x=input("Enter site::")
	r=requests.get("https://api.hackertarget.com/bannerlookup/?q="+str(x))
	print(r.text)
	
def geoip():
	x=input("Enter site::")
	r=requests.get("https://api.hackertarget.com/geoip/?q="+str(x))
	print(r.text)

def back():
	back=input("\nDo yo want to continue(y or n):: ")	
	if back=='y':
		clear()
		logo()
		menu()
	elif back=='n':
		exit()	

clear()			
logo()
menu()

