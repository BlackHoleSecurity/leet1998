## whatcms.rb - Detect CMS
## Detect Content Management Systems
require "uri"
require "json"
require "net/http"

__date__ = "12-July-2018"
__author__ = "DedSecTL/DTL"
__team__ = "BlackHole Security"
__codename__ = "Detect CMS"
__banner__ = """
################################################
#      Detect Content Management Systems       #
#              BlackHole Security              #
#               12 - July - 2018               #
################################################\n\n"""

@whatcmsAPIKey = "ENTER_YOUR_API_KEY_HERE"

def whatcms(target)
	request = Net::HTTP.get_response(URI("https://whatcms.org/APIEndpoint/Detect?key=#{@whatcmsAPIKey}&url=#{ARGV[0]}"))
	data = JSON.parse(request.body)
	if data["result"]["msg"] != "Success"
		puts data["result"]["msg"]
	else
		puts "Confidence: #{data["result"]["confidence"]}"
		puts "Code: #{data["result"]["code"]}"
		puts "Name: #{data["result"]["name"]}"
		puts "CMS URL: #{data["result"]["cms_url"]}"
		puts "Version: #{data["result"]["version"]}"
		puts "MSG: #{data["result"]["msg"]}"
		puts "ID: #{data["result"]["id"]}"
		puts "=======\nRequest web: #{data["request_web"]}"
	end
end

if __FILE__ == $0
	begin
		puts __banner__
		if ARGV.length != 1
			puts "Usage: whatcms www.example.com"
		else
			whatcms(ARGV[0])
		end
	rescue SocketError
		puts "whatcms: check your internet connection"
	end
end