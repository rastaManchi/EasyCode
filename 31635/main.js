const canvas = document.getElementById("game")
const ctx = canvas.getContext('2d')

let x = canvas.width / 2;
let y = canvas.height / 2;
const speed = 5;
let dx = 0;
let dy = 0;

// Враг
let enemyX = canvas.width / 4;
let enemyY = 50;
const enemyWidth = 80;
const enemyHeight = 50;
let enemySpeed = 2;
let enemyDx = enemySpeed;

// Функция для рисования квадрата
function drawSquare() {
    ctx.fillStyle = 'purple';
    ctx.fillRect(x, y, 50, 50);
}

// Функция для рисования врага
function drawEnemy() {
    ctx.fillStyle = 'red';
    ctx.fillRect(enemyX, enemyY, enemyWidth, enemyHeight);
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
    }
    if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
        dy = 0;
    }
}

// Подписка на события клавиатуры
document.addEventListener('keydown', keyDownHandler);
document.addEventListener('keyup', keyUpHandler);

// Проверка столкновений
function checkCollision() {
    if (x < enemyX + enemyWidth && x + 50 > enemyX && y < enemyY + enemyHeight && y + 50 > enemyY) {
        stopGame()
    }
}

// Остановка игры при столкновении
function stopGame() {
    dx = 0
    dy = 0
    enemyDx = 0
}

// Запуск анимации
function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawSquare();
    drawEnemy();
    checkCollision();

    x += dx;
    y += dy;

    // Обновление позиции врага
    enemyX += enemyDx;
    if (enemyX + enemyWidth > canvas.width || enemyX < 0) {
        enemyDx = -enemyDx;
    }
}

animate();
