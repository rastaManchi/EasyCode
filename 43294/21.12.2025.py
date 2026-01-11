class Matrix():
    def __init__(self, items):
        self.items = items
        
    
    def __add__(self, other):
        result = ''
        if type(other) == Matrix:
            if len(self.items) == len(other.items) and len(self.items[0]) == len(other.items[0]):
                for i in range(len(self.items)):
                    for j in range(len(self.items[0])):
                        result += f"{self.items[i][j] + other.items[i][j]}"
                    result += '\n'
        if result != '':
            return result
        return 'Неверные данные'
                    
                    
MatrixA = Matrix([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])

MatrixB = Matrix([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])

print(MatrixA+MatrixB)
