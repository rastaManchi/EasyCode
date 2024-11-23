const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

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


const image = new Image();
image.src = 'cursor.png';

let cursorImage = {
    x: 0,
    y: 0,
    width: 24,
    height: 24
}

canvas.addEventListener('mousemove', (event) => {
    const rect = canvas.getBoundingClientRect();
    cursorImage.x = event.clientX - rect.left - cursorImage.width/2;
    cursorImage.y = event.clientY - rect.top - cursorImage.height/2;
    draw();
})

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
        stopGame();
    }
}

// Остановка игры при столкновении
function stopGame() {
    dx = 0;
    dy = 0;
    enemyDx = 0;
}

// Запуск анимации
function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(image, cursorImage.x, cursorImage.y, cursorImage.width, cursorImage.height);
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

image.onload = animate();


// Управление на стрелочки

// let x = canvas.width / 2;
// let y = canvas.height / 2;

// const speed = 5;
// let dx = 0;
// let dy = 0;


// function drawcursorImage() {
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//     ctx.fillStyle = 'purple';
//     ctx.fillRect(x, y, 50, 50);
//     x += dx;
//     y += dy;
// }


// function keyDownHandler(event) {
//     if (event.key == 'ArrowRight') {
//         dx = speed;
//     } else if (event.key == 'ArrowLeft') {
//         dx = -speed;
//     } else if (event.key == 'ArrowUp') {
//         dy = -speed;
//     } else if (event.key == 'ArrowDown') {
//         dy = speed;
//     }
// }


// function keyUpHandler(event) {
//     if (event.key == 'ArrowRight' || event.key == 'ArrowLeft') {
//         dx = 0;
//     } else if (event.key == 'ArrowUp' || event.key == 'ArrowDown') {
//         dy = 0;
//     }
// }


// document.addEventListener('keydown', keyDownHandler);
// document.addEventListener('keyup', keyUpHandler);


// function animate() {
//     requestAnimationFrame(animate);
//     drawcursorImage();
// }


// animate()




