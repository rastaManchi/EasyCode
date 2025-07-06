let currentWord = 0;
let score = 0;
const dictionary = [
    { english: "apple", russian: "яблоко" },
    { english: "tree", russian: "дерево" },
    { english: "sun", russian: "солнце" }
];

function showNextWord() {
    document.getElementById('wordToTranslate').textContent = dictionary[currentWord].english;
    document.getElementById('userInput').value = '';
    document.getElementById('feedback').textContent = '';
    document.getElementById('checkButton').disabled = true;
}

function checkTranslation() {
    const userTranslation = document.getElementById('userInput').value;
    if (userTranslation.toLowerCase() === dictionary[currentWord].russian.toLowerCase()) {
        document.getElementById('feedback').textContent = 'Верно!';
        score += 10;
        currentWord++;
        setTimeout(showNextWord, 1500);
    } else {
        document.getElementById('feedback').textContent = 'Неверно, попробуйте еще раз.';
    }
    document.getElementById('score').textContent = `Очки: ${score}`;
}

function enableCheckButton() {
    if (document.getElementById('userInput').value.trim() !== '') {
        document.getElementById('checkButton').disabled = false;
    } else {
        document.getElementById('checkButton').disabled = true;
    }
}

function showAnswer() {
    document.getElementById('feedback').textContent = `Правильный ответ: ${dictionary[currentWord].russian}`;
    currentWord++;
    setTimeout(showNextWord, 1500);
}

window.onload = showNextWord;
document.getElementById('userInput').addEventListener('input', enableCheckButton);





