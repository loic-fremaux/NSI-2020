cache = [2]


def is_prime(n):
    for m in range(2, n):
        if n % m == 0:
            return False
    return True


def prime_list(n):
    print("cache: ", cache)
    for k in range(cache[len(cache) - 1] + 1, n):
        if is_prime(k):
            cache.append(k)
    return cache


for i in range(3, 10_000_000, 2):
    f = False
    for e in range(0, 21):
        e = 2 ** e
        for p in prime_list(i):
            print("{} != {} + {}".format(i, e, p))
            if i == e + p:
                f = True
                break
    if not f:
        exit("Exception: {}".format(i))

