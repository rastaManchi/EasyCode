const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

const tankImage = new Image();
tankImage.src = 'tank.png'; // Убедитесь, что путь к изображению правильный

const bulletImage = new Image();
bulletImage.src = 'bullet.png'; // Убедитесь, что путь к изображению правильный

const explosionImage = new Image();
explosionImage.src = 'explosion.png'; // Убедитесь, что путь к изображению правильный

const enemyTankImage = new Image();
enemyTankImage.src = 'enemy_tank.png'; // Убедитесь, что путь к изображению правильный

const tank = {
    x: 400,
    y: 500,
    width: 50,
    height: 50
};

const bullets = [];
let explosion = null;

const enemyTank = {
    x: 400,
    y: 100,
    width: 50,
    height: 50,
    lives: 3,
    alive: true
};

document.addEventListener('click', (event) => {
    shootBullet(event.clientX, event.clientY);
});

function shootBullet(targetX, targetY) {
    const startX = tank.x + tank.width / 2;
    const startY = tank.y + tank.height / 2;
    const angle = Math.atan2(targetY - startY, targetX - startX);

    bullets.push({
        x: startX,
        y: startY,
        width: 10,
        height: 10,
        speed: 5,
        dx: Math.cos(angle) * 5,
        dy: Math.sin(angle) * 5
    });
}

function updateBullets() {
    bullets.forEach((bullet, index) => {
        bullet.x += bullet.dx;
        bullet.y += bullet.dy;
        if (bullet.x + bullet.width < 0 || bullet.x > canvas.width ||
            bullet.y + bullet.height < 0 || bullet.y > canvas.height) {
            bullets.splice(index, 1);
        }
    });
}

function drawTank() {
    ctx.drawImage(tankImage, tank.x, tank.y, tank.width, tank.height);
}

function drawBullets() {
    bullets.forEach(bullet => {
        ctx.drawImage(bulletImage, bullet.x, bullet.y, bullet.width, bullet.height);
    });
}

function drawEnemyTank() {
    if (enemyTank.alive) {
        ctx.drawImage(enemyTankImage, enemyTank.x, enemyTank.y, enemyTank.width, enemyTank.height);
    }
}

function drawEnemyLives() {
    ctx.font = '20px Arial';
    ctx.fillStyle = 'red';
    ctx.fillText(`Lives: ${enemyTank.lives}`, enemyTank.x, enemyTank.y - 10);
}

function checkBulletCollision() {
    bullets.forEach((bullet, bulletIndex) => {
        if (enemyTank.alive && bullet.x < enemyTank.x + enemyTank.width &&
            bullet.x + bullet.width > enemyTank.x &&
            bullet.y < enemyTank.y + enemyTank.height &&
            bullet.y + bullet.height > enemyTank.y) {
            // Пуля попала во вражеский танк
            enemyTank.lives -= 1;
            bullets.splice(bulletIndex, 1);

            if (enemyTank.lives <= 0) {
                enemyTank.alive = false;
                // Создание взрыва
                explosion = {
                    x: enemyTank.x + enemyTank.width / 2 - 25,
                    y: enemyTank.y + enemyTank.height / 2 - 25,
                    size: 50,
                    duration: 30
                };
                alert('Вы выиграли!');
            }
        }
    })
};


function drawExplosion() {
    if (explosion) {
        ctx.drawImage(explosionImage, explosion.x, explosion.y, explosion.size, explosion.size);
        explosion.duration -= 1;

        if (explosion.duration <= 0) {
            explosion = null;
        }
    }
}

function update() {
    updateBullets();
    checkBulletCollision();

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawTank();
    drawBullets();
    drawEnemyTank();
    if (enemyTank.alive) {
        drawEnemyLives();
    }
    drawExplosion();

    requestAnimationFrame(update);
}

// Запуск игры после загрузки всех изображений
window.onload = () => {
    update();
};
