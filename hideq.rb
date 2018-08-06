## hideq.rb - Hidden Pages/Files Finder
## URL Fuzzer
require "uri"
require "net/http"

__date__ = "27-July-2018"
__author__ = "DedSecTL/DTL"
__team__ = "BlackHole Security"
__codename__ = "Shitty thing happen here"
__banner__ = """
################################################
#           Hidden Pages/Files Finder          #
#              BlackHole Security              #
#               27 - July - 2018               #
################################################\n\n"""

def hideq(target)
	path = "/backups,/index.php.old,/archive.tgz,/source_code.zip,/gallery1.html,/gallery2.html,/gallery3.html,/gallery4.html,/form-name,/client-resources/article-title,/product-name,/newsletter,/content/backups,/content/index.php.old,/content/archive.tgz,/content/source_code.zip,/content/gallery1.html,/content/gallery2.html,/content/gallery3.html,/content/gallery4.html,/content/form-name,/content/client-resources/article-title,/content/product-name,/content/newsletter"
	path.split(",").each do |n|
		res = Net::HTTP.get_response(URI("http://"+target+n))
		puts "Url: http://"+target+n
		puts "Header: "+res.code
	end
end

if __FILE__ == $0
	puts __banner__
	if ARGV.length != 1
		puts "Usage: hideq www.example.com"
	else
		hideq(ARGV[0])
	end
end