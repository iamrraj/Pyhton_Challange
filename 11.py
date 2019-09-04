from itertools import groupby
from functools import reduce

# print(len(reduce(lambda x, n:reduce(lambda a, b: a + str(len(list(b[1]))) + b[0], groupby(x), ""), range(30), "1")))
x = "1"
for n in range(30):
    x = "".join([str(len(list(j))) + i for i,j in groupby(x)])
    print(len(x))