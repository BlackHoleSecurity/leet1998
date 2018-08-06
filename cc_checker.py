## cc_checker.py - Credit Card Checker
# -*- coding: utf-8 -*-
##
import sys
import requests
from bs4 import BeautifulSoup as bs

__date__ = "29-July-2018"
__author__ = "DedSecTL/DTL"
__team__ = "BlackHole Security"
__codename__ = "Validate the CC!!"
__banner__ = """
################################################
#             Credit Card Checker              #
#              BlackHole Security              #
#               29 - July - 2018               #
################################################
"""

def cc_checker(list):
	for cc in open(list, 'r').read().split():
		r = requests.get('http://validate.creditcard/number/'+cc+'/')
		if "Congratulations!" in r.text:
			print "[*] CC :",cc
			print "[*] Status :",bs(r.text, 'html5lib').find('h2').text+"\n"
		elif "Formatting Error" in r.text:
			print "[*] CC :",cc
			print "[*] Status :",bs(r.text, 'html5lib').find('h3').text+"\n"
		else:
			print "[*] CC :",cc
			print "[*] Status :",bs(r.text, 'html5lib').find('h2').text+"\n"

if __name__ == '__main__':
	print __banner__
	if len(sys.argv) != 2:
		print "Usage: cc_checker creditcardlist.txt"
	else:
		cc_checker(sys.argv[1])