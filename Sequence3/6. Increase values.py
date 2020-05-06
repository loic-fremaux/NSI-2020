def increase(args):
    for i in range(len(args)):
        args[i] = args[i] + 1
    return args


numbers = [1, 2, 3, 4]
print(increase(numbers))
