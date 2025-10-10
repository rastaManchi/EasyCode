let high = prompt("Введите высоту: ")
let width = prompt("Введите ширину: ")

for (let i = 1; i<=high; i++) {
    let row = ""
    for (let j = 1; j<=width; j++) {
        row += "*"
    }
    console.log(row)
    console.log("")
}
