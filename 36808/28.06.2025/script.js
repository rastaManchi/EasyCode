let users = ['Ренат', 'Егор', 'Кирилл Г']
users.push('Георгий') // Добавить
users.push('Кирилл')
users.push('Артем')
users.pop() //Удалить последний элемент
users.pop()
console.log(users)
console.log(users.length)

users.splice(4, 0, 'Артем', 'Кирилл') // Добавить
console.log(users)
users.push('Булат')
console.log(users)

users.splice(6, 1, 'Елена') // Замена
console.log(users)

users.splice(6, 1) // Удаление
console.log(users)