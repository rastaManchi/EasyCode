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

// const btn = document.getElementById('btn')
// btn.addEventListener('click', () => {
    
//     let div_block = document.createElement('div')
//     div_block.classList.add('module')

//     let text = document.createElement('h2')
//     text.textContent = 'Новый текст'

//     div_block.appendChild(text)

//     document.body.appendChild(div_block)
// })


// #######################################

// if (2==2) {
//     alert('Круто')
// }
// else if (3==2) {
//     alert('Норм')
// }
// else {
//     alert('не круто')
// }


// for (let i=0; i<10; i++) {
//     alert(i)
// }


// let a = ['Булат', 'Вадим']

// for (let name in a) {
//     alert(name)
// }
// in -- проход по индексам 0..1
// of -- проход по значениям Булат..Вадим

// while ('Булат' in a) {
//     console.log('Привет')
// }

fetch('/buy', {
    method: 'POST',
    body: JSON.stringify({"item_id": 2})
})
.then(response => {
    console.log(response.json())
})