let score = 60

if (score >= 90) {
    console.log("Отлично!")
}
else if (score >= 80) {
    console.log("Хор")
}
else if (score >= 70) {
    console.log("Удовл")
}
else {
    console.log("Не сдал!")
}

// if; else if; else
// ==
// !=
// >
// <
// >=
// <= 

let day = 3

switch (day) {
    case 1:
        console.log('Понедельник')
    case 2:
        console.log('Вторник')
    case 3:
        console.log('Среда')
    default:
        console.log('Неизвестный день')
}

// или - ||
// и - &&

let weather = 'солнечно'
let dz = 'сделано'

if (weather != 'дождь' && dz == 'сделано') {
    alert('Идем гулять')
}

const name = prompt('Как вас зовут: ')
console.log(name)

