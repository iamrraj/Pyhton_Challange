import urllib.request
import re

page = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').readlines() #[38:]
print("The url is " + "".join(re.findall(r"[a-z]+", ''.join(page))) + ".html")
