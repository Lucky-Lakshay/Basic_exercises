# Objective- find factorial of a given number


def factorial_of(n):
    factorial = 1
    if n < 0:
        print("Factorial is not defined for negative integers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, n + 1):
            factorial *= i
        print(f"The factorial of {n} is {factorial}")


factorial_of(0)
factorial_of(-3)
factorial_of(5)
