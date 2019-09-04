from PIL import Image
import urllib.request
import re

#download the image
image_file = 'oxygen.png'
urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/' + image_file, image_file)

im = Image.open(image_file, 'r')

pix = im.load()

(width, hight) = im.size 
print("Image size: " + str((width, hight)))

output1 = ''.join([chr(pix[i,hight/2][0]) for i in range(0, width, 7)])
print(output1)


output2 = re.search(r'\[(.*?)\]', output1).group(1)
print("\nThe url is " + ''.join([chr(int(i)) for i in output2.split(',')]) + ".html")