## myip.py - Check your IP address
# -*- coding: utf-8 -*-
##
import requests

__date__ = "1-July-2018"
__author__ = "DedSecTL/DTL"
__team__ = "BlackHole Security"
__codename__ = "CYIA"
__banner__ = """
################################################
#             Check your IP address            #
#              BlackHole Security              #
#               1 - July - 2018                #
################################################
"""

def myip():
	r = requests.get('https://api.myip.com')
	print "\nMyIP: IP:\033[93m",r.json()["ip"],"\033[0m"
	print "MyIP: Country:\033[93m",r.json()["country"],"\033[0m"
	print "MyIP: Country Code:\033[93m",r.json()["cc"],"\033[0m"

if __name__ == '__main__':
	print __banner__
	raw_input("Press ENTER to Continue...")
	myip()