# recursive function that calculates the sum of numbers from 0 to 10
def addition(n):
    if n == 0:
        return 0
    else:
        return n + addition(n - 1)


print(addition(10))
