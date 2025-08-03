const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');

const tankImage = new Image();
tankImage.src = 'Exclude.png';

const bulletImage = new Image();
bulletImage.src = 'Exclude.png'

const tank = {
    x: 400,
    y: 500,
    width: 50,
    height: 50
}

const bullets = [];

document.addEventListener('click', () => {
    shootBullet();
})

function shootBullet() {
    bullets.push({
        x: tank.x + tank.width / 2,
        y: tank.y,
        width: 10,
        height: 10,
        speed: 5
    })
}

function updateBullet() {
    bullets.forEach((bullet, index) => {
        bullet.y -= bullet.speed;
        if (bullet.y + bullet.height < 0) {
            bullets.splice(index, 1)
        }
    })
}

function drawBullet() {
    bullets.forEach((bullet, index) => {
        ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
        //ctx.drawImage(bulletImage, bullet.x, bullet.y, bullet.width, bullet.height)
    })
}

function drawTank() {
    ctx.fillRect(tank.x, tank.y, tank.width, tank.height)
    // ctx.drawImage(tankImage, tank.x, tank.y, tank.width, tank.height)
}


function update() {
    updateBullet();
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawTank()
    drawBullet()

    requestAnimationFrame(update)
}


window.onload = () => {
    update();
}