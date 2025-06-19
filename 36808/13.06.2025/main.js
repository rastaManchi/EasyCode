const resultField = document.getElementById('resultMessage')
let randomNumber = Math.floor(Math.random() * 100) + 1
let currentTry = 0
let maxtries = 10

function CheckGuess() {
    if (currentTry < maxtries) {
        const guessField = document.getElementById('guessField')// '  52 '
        let usernumber = guessField.value.trim() // '52'
        let chislousernumber = parseInt(usernumber) // 52
        if (chislousernumber == randomNumber) {
            // alert("Победа")
            resultField.textContent = 'Победа'
        }
        else if (chislousernumber > randomNumber) {
            // alert('Загаданное меньше')
            resultField.textContent = 'Загаданное меньше'
        }
        else {
            // alert('Загаданное больше!')
            resultField.textContent = 'Загаданное больше!'
        }
        currentTry++
        document.getElementById('attemptsRemaining').textContent = `Осталось попыток: ${maxtries-currentTry}`
    }
    else {
        resultField.textContent = 'Попытки закончились'
    }
}

const guessSubmit = document.getElementById('guessSubmit')
guessSubmit.addEventListener('click', () => {
    CheckGuess()
})
// alt+Shift+F