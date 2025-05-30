const canvas = document.getElementById("game")
const ctx = canvas.getContext('2d')

const tankImage = new Image();
tankImage.src = 'wall.jpg';  

const bulletImage = new Image();
bulletImage.src = 'wall.jpg';  

const tank = {
    x: 400,
    y: 500,
    width: 50,
    height: 50
};

const Enemy_tank = {
    x: 400,
    y: 100,
    width: 50,
    height: 50,
    alive: true
};


const bullets = [];

document.addEventListener('click', (event) => {
    shootBullet(event.clientX, event.clientY);
});

function shootBullet(targetX, targetY) {
    const startX = tank.x + tank.width / 2 
    const startY = tank.y + tank.height / 2 
    const angle = Math.atan2(targetY-startY, targetX-startX)
    bullets.push({
        x: tank.x + tank.width / 2 - 5,
        y: tank.y,
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

function drawEnemyTank() {
    if (Enemy_tank.alive) {
        ctx.drawImage(tankImage, Enemy_tank.x, Enemy_tank.y, Enemy_tank.width, Enemy_tank.height);
    }
}


function drawBullets() {
    bullets.forEach(bullet => {
        ctx.drawImage(bulletImage, bullet.x, bullet.y, bullet.width, bullet.height);
    });
}

function update() {
    updateBullets();
    // проверка столкновения пули с врагом, например checkCollision()

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawTank();
    drawEnemyTank();
    drawBullets();

    requestAnimationFrame(update);
}

window.onload = () => {
    update();
};
