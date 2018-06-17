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

def get_lowest_lexical_order(set1, set2):
    pass

N, M, D = (int(i) for i in input().split())
T = (int(i) for i in input().split())

min_set = ()
min_ugliness = 100000
for i in itertools.combinations(T, N):
    current_ugliness = calculate_ugliness(i, D)
    if current_ugliness <= min_ugliness:
        if current_ugliness == min_ugliness:
            min_set = get_lowest_lexical_order(i, previous_min_ugliness)
        min_ugliness = current_ugliness
        previous_min_ugliness_set = i

print(calculate_ugliness((1, 4, 3, 2), 2))
print(calculate_ugliness((1, 4, 5, 3), 2))
# print(max_set)
