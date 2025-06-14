# new commands: git pull
import math


def isPrime(n):
    if n == 0 or n == 1:
        return True

    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# I think something is amiss, hmmmm...
for i in range(0, 20):
    if isPrime(i):
        print(f"{i} is NOT a prime number")
    else:
        print(i)
