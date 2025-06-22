// В IT компании "Tech Innovators" каждый сотрудник получает бонус за каждый год работы.
// Вам нужно написать программу, которая выводит бонусы для сотрудников, проработавших от 1 до 5 лет. 
// Бонус за каждый год составляет 1000 долларов.

// Инструкция:  
// - Используйте цикл for, чтобы пройтись по каждому году от 1 до 5.
// - Выведите сообщение в консоль с указанием года и соответствующего бонуса.

// let max_year = 5
// let bonus = 0

// for (let year=1; year<=max_year; year++){
//     bonus += 1000
//     console.log(`Год: ${year} | Бонус: ${bonus}$`)
// }


// let principal = parseFloat(prompt("Введите начальную сумму вклада:"));
// let rate = parseFloat(prompt("Введите годовую процентную ставку (в процентах):")) / 100;
// let years = parseInt(prompt("Введите количество лет:"));
// let currentYear = 0;
// while (currentYear < years) {
//     principal += principal * rate;
//     currentYear++;
// }
// alert(`Сумма вклада через ${years} лет: ${principal.toFixed(2)}`);


// let accountBalance = 1000;
// let summ;
// while (accountBalance > 0) {
//     summ = parseInt(prompt(`Введите сумму (Ваш баланс ${accountBalance}): `))
//     if (accountBalance>=summ) {
//         accountBalance -= summ
//     }
// } 

// alert(`Процесс завершен. Остаток на счете: ${accountBalance}`);
let i = 0
for (i; i < 5; i++) {
    console.log(i)
}
console.log(i)