import urllib
import re

nothing = "12345"
#nothing = str(16044/2)
while True:
    four = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing).read()
    print(four)
    nott = re.search(r"(\d+)",four)
    if nott == None:
        break
    nothing = nott.group(1)
    