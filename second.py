# from functools import reduce

# print(len(reduce(lambda x, n:reduce(lambda a, b: a + str(len(list(b[1]))) + b[0], groupby(x), ""), range(30), "1")))


input_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


url = "map"
s = {'a':'c', 'b':'d', 'c':'e', 'd':'f', 'e':'g', 'f':'h', 'g':'i', 'h':'j', 'i':'k', 'j':'l',\
        'k':'m', 'l':'n', 'm':'o', 'n':'p', 'o':'q', 'p':'r', 'q':'s', 'r':'t', 's':'u', 't':'v',\
        'u':'w', 'v':'x', 'w':'y', 'x':'z', 'y':'a','z':'b', ' ':' ', '.':'.', "'":"'", '(':'(', ')':')'}

def main():
    ans = ""
    for c in url:
        ans += s[c]
    print(ans)

main()