# Objective- Reverse a given integer using while Loop
Given_int = 1234567
reversed_int = 0

while Given_int > 0:
    rem = Given_int % 10
    reversed_int = (reversed_int * 10) + rem
    Given_int = Given_int // 10

print(reversed_int)
