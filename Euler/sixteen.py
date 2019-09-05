def euler():
    number = 2 ** 1000
    ans = sum(int(c) for c in str(number))
    return str(ans)
    

if __name__ == "__main__":
	print(euler())