import urllib
import re

page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').readlines() #[38:]
print("The url is " + "".join(re.findall(r"[a-z]+", ''.join(page))) + ".html")
# print "".join(re.findall("[A-Za-z]", data))