# creating fibonacci series till "n" terms if first and second terms of series is given
term_1 = 0
term_2 = 1
n = 20
for i in range(n):
    print(term_1, end=" ")
    term_3 = term_1 + term_2

    term_1 = term_2
    term_2 = term_3
