import urllib.request
import re
import pickle

text = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
data = pickle.loads(text)

for row in data:
  print(''.join([p[0] * p[1] for p in row]))