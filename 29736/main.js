const canvas = document.getElementById('gameCanvas')
const ctx = canvas.getContext('2d')


// ctx.fillStyle = 'green'
// ctx.fillRect(10, 10, 100, 100)

// ctx.strokeStyle = 'red'
// ctx.strokeRect(150, 10, 100, 100)

// ctx.clearRect(20, 20, 30, 30)


// ctx.beginPath()
// ctx.moveTo(50, 50)
// ctx.lineTo(200, 50)
// ctx.stroke()
// ctx.closePath()


// ctx.beginPath()
// ctx.moveTo(250, 50)
// ctx.lineTo(300, 200)
// ctx.lineTo(400, 200); // Правая нижняя вершина
// ctx.lineTo(320, 275); // Нижняя вершина
// ctx.lineTo(350, 400); // Левая нижняя вершина
// ctx.lineTo(250, 325); // Левая верхняя вершина
// ctx.lineTo(150, 400); // Верхняя вершина
// ctx.lineTo(180, 275); // Правая верхняя вершина
// ctx.lineTo(100, 200); // Правая нижняя вершина
// ctx.lineTo(200, 200); // Левая верхняя вершина
// ctx.closePath(); // Заканчиваем путь
// ctx.strokeStyle = 'red'
// ctx.stroke()
// ctx.fillStyle = 'yellow'
// ctx.fill()


// ctx.beginPath()
// ctx.arc(100, 75, 50, 0, Math.PI , true)
// ctx.fillStyle = 'blue'

// ctx.closePath()
// ctx.fill()


// ctx.beginPath();
// ctx.arc(250, 250, 100, 0, Math.PI, true);
// ctx.fillStyle = 'purple';
// ctx.fill();
// ctx.stroke();


// ctx.beginPath()
// ctx.quadraticCurveTo(100, 10, 200, 50)
// ctx.closePath()
// ctx.stroke()


// ctx.beginPath();
// ctx.moveTo(120, 250); // Нижняя левая точка облака
// ctx.bezierCurveTo(100, 230, 140, 200, 180, 220); // Левая верхняя часть
// ctx.bezierCurveTo(220, 180, 280, 180, 320, 220); // Верхняя часть облака
// ctx.bezierCurveTo(360, 200, 400, 230, 380, 250); // Правая верхняя часть
// ctx.bezierCurveTo(420, 290, 360, 320, 320, 300); // Правая нижняя часть
// ctx.bezierCurveTo(280, 340, 220, 340, 180, 300); // Нижняя часть облака
// ctx.bezierCurveTo(140, 320, 100, 290, 120, 250); // Левая нижняя часть
// ctx.closePath();
// ctx.fillStyle = 'lightgray';
// ctx.fill();
// ctx.strokeStyle = 'gray';
// ctx.stroke();


const spriteSheet = new Image()
spriteSheet.src = "i.webp"

const spriteWidth = 41.8
const spriteHeight = 92
let currentFrame = 0
const totalFrames = 20

const animationSpeed = 100

let x = 0
let y = 0

spriteSheet.onload = function () {
    setInterval(animateSprite, animationSpeed)
}

function animateSprite() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Очистка Canvas
       
    // Вычисляем координаты текущего кадра на спрайт-листе
    const frameX = currentFrame * spriteWidth;
    
    // Рисуем текущий кадр
    ctx.drawImage(spriteSheet, frameX, 0, spriteWidth, spriteHeight, x, y, spriteWidth, spriteHeight);

    // Переход к следующему кадру
    currentFrame = (currentFrame + 1) % totalFrames;

}

spriteSheet.onerror = function () {
    console.log('Ошибка загрузки спрайта')
}