# 1. NON(A ET B) = NON(A) OU NON(B)
#
# | A | B | NON(A ET B) | NON(A) OU NON(B) |
# | 0 | 0 | 1           | 1                |
# | 0 | 1 | 1           | 1                |
# | 1 | 0 | 1           | 1                |
# | 1 | 1 | 0           | 0                |

# 2. NON(NON(A) ET NON(B))
#  > A OR B
#    NON(NON(A) OU NON(B))
#  > A AND Q
#    NON(A OU B) ET A
#  > ALWAYS FALSE

# Test program
tests = [
    [False, False],
    [False, True],
    [True, False],
    [True, True]
]

for g in tests:
    p = g[0]
    q = g[1]
    r1 = False
    if not(p or q) and p:  # first expression
        print("true for", g)
        r1 = True
    else:
        print("false for", g)
    r2 = False
    if p & q:  # second expression
        r2 = True
    if r1 != r2:
        print("not equals")
        break