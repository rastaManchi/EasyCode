a = {1, 2, 3}
b = {3, 4, 5}


a.union(b)
a.intersection(b)
a.symmetric_difference(b)
a.difference(b)


first_set = set(input())
second_set = set(input())
print(first_set.intersection(second_set))