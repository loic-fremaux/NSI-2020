def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


for x in range(1, 1000):
    for y in range(1, 1000):
        if 6 * (fact(x) + 3) == y ** 2 + 5:
            print(x, y)
