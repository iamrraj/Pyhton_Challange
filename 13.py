data = open("evil2.gfx", "rb").read()
print(len(data))
for i in range(5):
    open('%d.jpg' % i ,'wb').write(data[i::5])
