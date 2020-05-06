def average(tab):
    with_coefficient = [group[0] * group[1] for group in tab]
    coefficients = [group[1] for group in tab]
    return sum(with_coefficient) / sum(coefficients)


L = [[11, 2], [8, 4], [12, 3]]
print(average(L))
