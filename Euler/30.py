# import sys
# if sys.version_info.major == 2:
# 	range = xrange

def euler():
    ans = sum(i for i in range(2, 1000000) if i == fifth_power(i))
    return str(ans)

def fifth_power(n):
    return sum(int(c) ** 5 for c in str(n))


if __name__ == "__main__":
    print(euler())