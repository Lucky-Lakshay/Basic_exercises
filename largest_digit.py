# Find largest digit in a number
num1 = 9876543210
num2 = -5082

def largest(num):
    num = str(abs(num))
    largest_digit = int(num[0])
    for i in num[1:]:
        i = int(i)
        if i > largest_digit:
            largest_digit = i
    print(largest_digit)

largest(num1)
largest(num2)
