letters = list(sorted('ТЕОРИЯ'))
INDEX_MAX = len(letters) - 1

check_word = ['Е', 'Е', 'Е', 'Е', 'Е', 'Е']
result = 0

mnozh = set()

for start_letter in range(INDEX_MAX, -1, -1):
    print('_' * 20)
    check_word = ['Е', 'Е', 'Е', 'Е', 'Е', 'Е']
    for x1 in range(1, 6):
        check_word[start_letter] = letters[x1]
        if start_letter != INDEX_MAX:
            for letter in range(start_letter + 1, INDEX_MAX + 1):
                for x2 in range(6):
                    check_word[letter] = letters[x2]
                    print(check_word)
                    

print(mnozh)
                

    