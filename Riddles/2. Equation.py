# 1. Plutôt la valeur de transition ?
val = None
for i in range(100):
    for j in range(100):
        val = i + j
        if i * j < i + j:
            break


print("Valeur de transition:", val)

# 2.
c = 0
for i in range(10_000):
    for j in range(10_000):
        s = int(str(i) + str(j))
        if s - 12 == i * j:
            c += 1

print("Il y a", c, "résultats")
