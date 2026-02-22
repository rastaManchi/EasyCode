MA = [
    [2, 4],
    [4, 5]
]

MB = [
    [2, 5],
    [6, 7]
]

MC = [
    [],
    []
]

if len(MA) == len(MB) and len(MA[0]) == len(MB[0]):
    for row in range(len(MA)):
        summ = 0
        for column in range(len(MA[0])):
            summ += MA[row][column] * MB[column][row]
        print(summ)
else:
    print('Матрицы должны быть одинакого размера!')
    
    
col = int(input())
rows = int(input())
matrixUser = []
for row in range(rows):
    matrixUser.append([])
    for col_ in range(col):
        number = int(input())
        matrixUser[row].append(number)
        