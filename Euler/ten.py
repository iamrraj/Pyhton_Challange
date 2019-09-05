import eulerlib

def euler():
    ans = sum(eulerlib.prime_numbers.primes(1999999))
    return str(ans)

if __name__ == "__main__":
    print(euler())