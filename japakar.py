#!/usr/bin/python
# -*- coding: utf-8 -*-
# japakar.com auto claim
import time
import requests
from bs4 import BeautifulSoup as bs

__date__ = "27-July-2018"
__author__ = "DedSecTL/DTL"
__team__ = "BlackHole Security"
__codename__ = "Pemulung"
__banner__ = """
################################################
#             PemulungDOGEmahBebas             #
#              BlackHole Security              #
#               27 - July - 2018               #
################################################
"""

def autoclaim(address):
	while True:
		r = requests.get("http://auto1.japakar.com/faucet.php?address="+address+"&currency=DOGE&key=5705aad8e837f0036567f32bbd4cd4c3")
		response = bs(r.text, 'html5lib').find_all('div')
		try:
			print "\n\033[97mStatus:\033[92m Success claim "+str(str(response[23]).split(">")[1].split("<")[0].split()[0])+" satoshi to",address,"\033[0m"
			print "\033[97mAddress:\033[92m",address,"\033[0m"
			print "\033[97mResponse:\033[92m",str(str(response[23]).split(">")[1].split("<")[0]),"your account at FaucetHub.io\033[0m"
			print "\033[93mSleep for 60 Sec...\033[0m"
			time.sleep(60)
		except:
			print "\n\033[97mStatus: \033[91mNull\033[0m"
			print "\033[97mAddress:\033[92m",address,"\033[0m"
			print "\033[93mSleep for 60 Sec...\033[0m"
			time.sleep(60)
	
if __name__ == '__main__':
	print __banner__
	address = raw_input("Input Your DOGE Address: ")
	if address != None:
		autoclaim(address)
	else:
		print "Please enter your DOGE address" 