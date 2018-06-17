import itertools


def calculate_ugliness(T, D):
    ugliness = 0
    for i in itertools.combinations(T, 2):
        if sum(i) > D:
            ugliness += 1
    for i in T:
        if i + i > D:
            ugliness += 1
    return ugliness

N, M, D = (int(i) for i in input().split())
T = (int(i) for i in input().split())
print (T)
