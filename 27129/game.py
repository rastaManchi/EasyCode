file = open('27129/game.txt', 'r', encoding='utf-8')

# r - read only
# w - write only
# a - add only

# result = file.read()

# result = file.write('Булат!\n')
# print(result)

result = file.read()
print( result.split('\n') )
