# pattern:
# 1
# 6 1
# 10 5 1
# 13 8 4 1
# 15 10 6 3 1
# 16 11 7 4 2 1


def fun(n):
    a = 1
    for row in range(1, n + 1):
        val = a
        diff = 5
        for i in range(row):
            print(val, end=" ")
            val -= diff
            diff -= 1
        print()
        if row < n:
            a += 6 - row


fun(6)
