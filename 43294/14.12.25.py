matrix = [
    [1,2,3],
    [4,5234224,6],
    [7,8,9]
]

for spisokchek in matrix:
    for number in spisokchek:
        print(f"{number}".ljust(10), end=' ')
    print()