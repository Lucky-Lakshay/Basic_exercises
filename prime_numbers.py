# calculate prime numbers till "n" terms
# prime numbers are the numbers only divisible by 1 and itself
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


primes = []
num = 2
n = 20
while len(primes) <= n:
    if is_prime(num):
        primes.append(num)
    num += 1

print(primes)
