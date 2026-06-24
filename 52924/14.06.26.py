matrix = [
    [14534562343534, 2, 3],
    [4, 53453453534, 6],
    [7, 8, 9345345]
]


for row in matrix:
    for column in row:
        print(str(column).rjust(20), end=" ")
    print()