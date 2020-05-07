highest = 0
for i in range(0, 1_000_000):
    count = -1
    i = str(i)
    last = ""
    while i != last:
        tmp = 0
        for c in i:
            tmp += int(c)
        last = i
        i = str(tmp)
        count += 1
    if count > highest:
        highest = count

print("La plus grande persistance multiplicative est: ", highest)
