let day = 6


switch (day) {
    case 1:
        console.log('ПН')
        break
    case 2:
        console.log('ВТ')
        break
    case 3:
        console.log('СР')
        break
    case 4:
        console.log('ЧТ')
        break
    case 5:
        console.log('ПТ')
        break
    case 6:
        console.log('СБ')
        break
    case 7:
        console.log('ВС')
        break
}

// 3. Дана переменная, содержащая номер месяца. По этой переменной программа должна определить, какое сейчас время года.

let month = 3
let season
// && и
// || или
if (month === 12 || month === 1 || month === 2) {
    season = 'Зима'
}
else if (month === 3 || month === 4 || month === 5) {
    season = "Весна";
}
else if (month === 6 || month === 7 || month === 8) {
    season = "Лето";
}
else {
    season = "Осень";
}
  
console.log(`Сейчас ${season}`)



let num1 = prompt('Введите первое число: ')
let num2 = prompt('Введите второе число: ')
let sum = parseInt(num1) + parseInt(num2) // целые числа
let sum2 = parseFloat(num1) + parseFloat(num2) // дробные числа
alert('Сумма чисел: ' + sum)


