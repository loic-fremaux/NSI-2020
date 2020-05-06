def average(tab):
    return sum(tab) / len(tab)


def average_coefficient(tab):
    with_coefficient = [group[0] * group[1] for group in tab]
    coefficients = [group[1] for group in tab]
    return sum(with_coefficient) / sum(coefficients)


def variance(tab):
    squared = [k ** 2 for k in tab]
    return average(squared) - (average(tab) ** 2)


def variance_coefficient(tab):
    squared = [group[0] ** 2 for group in tab for k in range(group[1])]
    return average(squared) - (average_coefficient(tab) ** 2)


test = [1, 2, 3, 4, 5]
print(variance(test))

test = [[1, 5], [7, 4], [8, 2]]
print(variance_coefficient(test))
