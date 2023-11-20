n = int(input())

for i in range(n):
    for j in range(n - i, 0, -1):
        print(end=" ")

    coef = 1
    for j in range(i + 1):
        print(coef, end=" ")
        coef = coef * (i - j) // (j + 1)
    print()