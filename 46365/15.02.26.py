a = [
    [1, 2, 3],
    [4, 500, 6],
    [7, 8, 9000]
]

for row in a:
    for item in row:
        print(str(item).rjust(5), end=" ")
    print()