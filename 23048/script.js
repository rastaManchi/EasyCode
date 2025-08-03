// const a = 4
// let b = 10

// console.log('Hello World')
// alert('Hello world')

// let password = promt('Введи пароль: ')

// let str_b = b.toString()
// let int_password = parseInt(password)

// let spisok = []
// spisok.push('Элемент')
// console.log(spisok[0])

// spisok.pop()

// spisok.splice(0, 0, 'Другой элемент')

// let dictionary = {}
// dictionary.name = 'Булат'
// dictionary['name'] = 'Булат'

// console.log(dictionary.name)

// delete dictionary.name


// let struct = [
//     {
//         'name': 'Булат'
//     },
//     {
//         'name': 'Вадим'
//     }
// ]

// console.log(struct[1].name)

// ######################################

const btn = document.getElementById('btn')
btn.addEventListener('click', () => {
    
    let div_block = document.createElement('div')
    div_block.classList.add('module')

    let text = document.createElement('h2')
    text.textContent = 'Новый текст'

    div_block.appendChild(text)

    document.body.appendChild(div_block)
})
