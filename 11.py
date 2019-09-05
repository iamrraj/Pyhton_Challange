from itertools import groupby

x = "1"
for n in range(30):
    x = "".join([str(len(list(j))) + i for i,j in groupby(x)])
    print(len(x))