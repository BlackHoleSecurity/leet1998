import os, sys
import time
import base64
import requests

# recommend terminal like a-shell, iSH, etc
banner = """
# web clip app maker for iOS; author: Gameye98
# my profile: https://github.com/Gameye98
# date: Sun Mar 5 04:06:03 2023
-----
# schadenfreude: https://t.me/schdenfreude
# blackhole security: https://github.com/Gameye98/BlackHoleSecurity
"""

mobileconfig = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>ConsentText</key>
<dict>
<key>default</key>
<string>Choose 'Install' and enter passcode if prompted.</string>
</dict>
 <key>PayloadContent</key>
 <array>
   <dict>
     <key>FullScreen</key>
     <true/>
     <key>Icon</key>
     <data>{Base64 Encoded}</data>
     <key>IsRemovable</key>
     <true/>
     <key>Label</key>
     <string>{Name}</string>
     <key>PayloadDescription</key>
     <string>Turn any website into an app on your home screen</string>
     <key>PayloadDisplayName</key>
     <string>Web Clip ({Name})</string>
     <key>PayloadIdentifier</key>
     <string>Gameye98 - {UUID1}</string>
     <key>PayloadOrganization</key>
     <string>https://github.com/Gameye98 - {UUID1}</string>
     <key>PayloadType</key>
     <string>com.apple.webClip.managed</string>
     <key>PayloadUUID</key>
     <string>{UUID1}</string>
     <key>PayloadVersion</key>
     <integer>1</integer>
     <key>Precomposed</key>
     <false/>
     <key>URL</key>
     <string>{URL}</string>
   </dict>
 </array>
 <key>PayloadDescription</key>
 <string>Turn any website into an app on your home screen</string>
 <key>PayloadDisplayName</key>
 <string>{Name}</string>
 <key>PayloadIdentifier</key>
 <string>Gameye98 - {UUID1}</string>
 <key>PayloadOrganization</key>
 <string>https://github.com/Gameye98 - {UUID1}</string>
 <key>PayloadRemovalDisallowed</key>
 <false/>
 <key>PayloadType</key>
 <string>Configuration</string>
 <key>PayloadUUID</key>
 <string>{UUID2}</string>
 <key>PayloadVersion</key>
 <integer>1</integer>
</dict>
</plist>
"""

ls = os.getenv("PATH").split(":")

def find(filename):
	for i in ls:
		try:
			lsi = os.listdir(i)
		except (FileNotFoundError, PermissionError):
			continue
		for f in lsi:
			fname = f
			if "/" in fname:
				fname = fname.split("/")[-1]
			if fname == filename:
				return True
	return False

def profilegenerator(mobileconf):
	profile = base64.b64encode(mobileconf.encode("utf8")).decode()
	mime = "data:application/x-apple-aspen-config;base64,"
	print("[+] generate profile url: test.mobileconfig")
	open("test.mobileconfig","w").write(mime+profile)
	if find("open"):
		print("[+] opening the profile, waiting for user action...")
		os.system(f"open \"{mime+profile}\"")
		time.sleep(3)
		print("[!] if you still not redirected to the browser, then your 'open' command couldn't open the url")
	print("[!] you could copy the content of test.mobileconfig and paste it to the safari browser")

class UUID:
	def __init__(self):
		self.asciidat = __import__("string").digits+__import__("string").ascii_letters
		self.asciidat = [x for x in self.asciidat]
		while "" in self.asciidat: self.asciidat.remove("")
	def randomchar(self):
		return __import__("random").choice(self.asciidat)
	def v4generator(self):
		totalmax = 32
		fixedset = (8,12,16,20)
		self.result = ""
		while len(self.result.replace("-","")) < 32:
			if len(self.result.replace("-","")) in fixedset:
				self.result += "-" + self.randomchar()
				continue
			self.result += self.randomchar()

def main():
	global mobileconfig
	print(banner.strip()+"\n")
	appname = input("[*] app name: ")
	appicon = input("[*] app icon(url|file): ")
	appurl  = input("[*] app url : ")
	if os.path.isfile(appicon):
		appicon = open(appicon,"rb").read()
	elif appicon.startswith("http"):
		print("[+] downloading the app icon")
		appicon = requests.get(appicon).content
	else:
		print("[!] no such file exists or url invalid")
		return None
	print("[+] encoding the image (base64)")
	encoded = base64.b64encode(appicon).decode()
	mobileconfig = mobileconfig.replace("{Name}",appname)
	mobileconfig = mobileconfig.replace("{URL}",appurl)
	mobileconfig = mobileconfig.replace("{Base64 Encoded}",encoded)
	print("[+] generating UUID for uuid1: ", end="")
	uuid1 = UUID()
	uuid1.v4generator()
	print(uuid1.result)
	print("[+] generating UUID for uuid2: ", end="")
	uuid2 = UUID()
	uuid2.v4generator()
	print(uuid2.result)
	mobileconfig = mobileconfig.replace("{UUID1}",uuid1.result)
	mobileconfig = mobileconfig.replace("{UUID2}",uuid2.result)
	profilegenerator(mobileconfig)

if __name__ == "__main__":
	try:
		main()
	except (EOFError, KeyboardInterrupt):
		exit()