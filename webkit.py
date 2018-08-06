g = '\033[92;1m'
w = '\033[0m'
c = '\033[96;1m'

import requests
import optparse
import sys

def run(host,type,info):
	print g + ('Webkit' + w + ' | ' + g + info).center(60) + c + 'Telegram : @CiKu370' + w
	print (requests.get('https://api.hackertarget.com/' + type + '/?q=' + host).text)
def parse_cmd():

	k = 0
	p = optparse.OptionParser(c + 'WEBKIT' + w + ' | ' + c + 'basic information gathering for web' + w)
	p.add_option('-T',dest='hostname',help='Ip address or Domain name, required=True')

	p.add_option('-t','--traceroute',dest='traceroute',help='Traceroute Using MRT',action='store_true')
	p.add_option('-p','--ping',dest='ping',help='Test ping/Nping',action='store_true')
	p.add_option('-d','--dns-lookup',dest='dns',help='Dns Lookup',action='store_true')
	p.add_option('-r','--reverse-dns',dest='reversedns',help='Reverse Dns Lookup',action='store_true')
	p.add_option('-H','--host-records',dest='hostrecords',help='Find DNS Host Records',action='store_true')
	p.add_option('-s','--shared-dns',dest='shareddns',help='Find Shared DNS Servers',action='store_true')
	p.add_option('-z','--zone-test',dest='zone',help='Zone Transfer Test',action='store_true')
	p.add_option('-w','--whois',dest='whois',help='Whois Lookup',action='store_true')
	p.add_option('-g','--geoip',dest='geoip',help='GeoIP - IP Location Lookup',action='store_true')
	p.add_option('-i','--reverse-ip',dest='reverseip',help='Reverse IP Lookup',action='store_true')
	p.add_option('-n','--tcp-port',dest='tcp',help='TCP Port Scan',action='store_true')
	p.add_option('-S','--subnet',dest='subnet',help='Subnet Lookup',action='store_true')
	p.add_option('-C','--HTTP-Headers',dest='http',help='HTTP Header Check',action='store_true')
	p.add_option('-e','--extract-pages',dest='ex',help='Extract Links From Page',action='store_true')
	(opt,args) = p.parse_args()

	if opt.traceroute != None and opt.hostname != None:
		run(opt.hostname,'mtr','TRACEROUTE USING MTR')
		k += 1
	if opt.ping != None and opt.hostname != None:
                run(opt.hostname,'nping','TEST PING')
		k += 1
	if opt.dns != None and opt.hostname != None:
		run(opt.hostname,'dnslookup','DNS LOOKUP')
		k += 1
	if opt.reversedns != None and opt.hostname != None:
		run(opt.hostname,'reversedns','REVERSE DNS LOOKUP')
		k += 1
	if opt.hostrecords != None and opt.hostname != None:
		run(opt.hostname,'hostsearch','FIND DNS HOST RECORDS')
		k += 1
	if opt.shareddns != None and opt.hostname != None:
		run(opt.hostname,'findshareddns','FIND SHARED DNS SERVERS')
		k += 1
	if opt.zone != None and opt.hostname != None:
		run(opt.hostname,'zonetransfer','ZONE TRANSFER TEST')
		k += 1
	if opt.whois != None and opt.hostname != None:
		run(opt.hostname,'whois','WHOIS LOOKUP')
		k += 1
	if opt.geoip != None and opt.hostname != None:
		run(opt.hostname,'geoip','GEOIP - IP LOCATION LOOKUP')
		k += 1
	if opt.reverseip != None and opt.hostname != None:
		run(opt.hostname,'reverseiplookup','REVERSE IP LOOKUP')
		k += 1
	if opt.tcp != None and opt.hostname != None:
		run(opt.hostname,'nmap','TCP PORT SCAN')
		k += 1
	if opt.subnet != None and opt.hostname != None:
		run(opt.hostname,'subnetcalc','SUBNET LOOKUP')
		k += 1
	if opt.http != None and opt.hostname != None:
		run(opt.hostname,'httpheaders','HTTP HEADERS CHECK')
		k += 1
	if opt.ex != None and opt.hostname != None:
		run(opt.hostname,'pagelinks','EXTRACT LINK FROM PAGES')
		k += 1
	if k == 0 and opt.hostname != None or opt.hostname == None:
                print p.usage
		print 'Usage: %s -h/--help to show help message'%(sys.argv[0])
if __name__ == '__main__':
	parse_cmd()

