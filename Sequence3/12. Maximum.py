
def maximum(tab):
    maxi = float('-inf')
    for i in tab:
        if i > maxi:
            maxi = i

    return maxi


test = [1, 8, 12, 17, 3]
print(maximum(test))
