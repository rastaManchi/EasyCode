const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
let x = canvas.width / 2;
let y = canvas.height / 2;
const speed = 5;
let dx = 0;
let dy = 0;

// Функция для рисования квадрата
function drawSquare() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Очистка канваса
    ctx.fillStyle = 'purple'; // Цвет квадрата
    ctx.fillRect(x, y, 50, 50); // Рисуем квадрат
    x += dx;
    y += dy;
}

// Обработка нажатия к лавиш
function keyDownHandler(event) {
    if (event.key === 'ArrowRight') {
        dx = speed;
    } else if (event.key === 'ArrowLeft') {
        dx = -speed;
    } else if (event.key === 'ArrowUp') {
        dy = -speed;
    } else if (event.key === 'ArrowDown') {
        dy = speed;
    }
}

// Обработка отпускания клавиш
function keyUpHandler(event) {
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
        dx = 0;
    } else if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
        dy = 0;
    }
}

// Слушатель на события клавиатуры
document.addEventListener('keydown', keyDownHandler);
document.addEventListener('keyup', keyUpHandler);

// Запуск анимации
function animate() {
    requestAnimationFrame(animate);
    drawSquare();
}

animate();

