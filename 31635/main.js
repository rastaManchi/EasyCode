// for (let i = 1; i<=20; i++) {
//     if (i % 2 == '0') {
//         console.log(i)
//     }
// }


// for (let i = 1; i <= 10; i++) {
//     let row = '';
//     for (let j = 1; j <= 10; j++) {
//         row += (i*j) + '\t'
//     }
//     console.log(row)
// }


let width = 10
let height = 5


for (let i = 1; i <= height; i++) {
    let row = ''
    for (let j = 1; j <= width; j++) {
        row += '*'
    }
    console.log(row)
}