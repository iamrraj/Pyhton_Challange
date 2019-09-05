import math

def euler():
    f = math.factorial(100)
    ans = sum(int(c) for c in str(f))
    return str(ans)


if __name__ == "__main__":
    print(euler())