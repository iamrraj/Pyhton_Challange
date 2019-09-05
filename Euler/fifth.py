import math

def euler():
	ans = 1
	for i in range(1, 21):
		ans *= i // math.gcd(i, ans)
	return str(ans)


if __name__ == "__main__":
	print(euler())