const canvas = document.getElementById('my_game');
const ctx = canvas.getContext('2d');
let x = canvas.width / 2;
let y = canvas.height / 2;
const speed = 5;
let dx = 0;
let dy = 0;

let enemy = {
    x: 0,
    y: 100,
    dx: 2,
}


// Функция для рисования квадрата
function drawSquare() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Очистка канваса
    ctx.fillStyle = 'purple'; // Цвет квадрата
    ctx.fillRect(x, y, 50, 50); // Рисуем квадрат
    x += dx;
    y += dy;
}


function drawEnemy() {
    ctx.fillStyle = 'red'
    ctx.fillRect(enemy.x, enemy.y, 100, 50)
    enemy.x += enemy.dx
    if (enemy.x >= 1920 || enemy.x <= -50) {
        enemy.dx = -enemy.dx
    }
}


function checkCollision() {
    if (x < enemy.x + 50 && enemy.x < x + 50 && y < enemy.y + 50 && enemy.y < y + 50) {
        dx=0
        dy=0 
        enemy.dx = 0
    }
}


// Обработка нажатия клавиш
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
    drawEnemy();
    checkCollision()
}

animate();
