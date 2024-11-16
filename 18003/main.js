const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d')


ctx.beginPath();
// ctx.quadraticCurveTo(100, 0, 100, 300);
ctx.moveTo(120, 250); // Нижняя левая точка облака
ctx.bezierCurveTo(100, 230, 140, 200, 180, 220); // Левая верхняя часть
ctx.bezierCurveTo(220, 180, 280, 180, 320, 220); // Верхняя часть облака
ctx.bezierCurveTo(360, 200, 400, 230, 380, 250); // Правая верхняя часть
ctx.bezierCurveTo(420, 290, 360, 320, 320, 300); // Правая нижняя часть
ctx.bezierCurveTo(280, 340, 220, 340, 180, 300); // Нижняя часть облака
ctx.bezierCurveTo(140, 320, 100, 290, 120, 250); // Левая нижняя часть
ctx.fillStyle = 'lightgray';
ctx.fill();
ctx.strokeStyle = 'gray';
ctx.stroke();

// const player = new Image();
// player.src = 'enemy.png';
// player.onload = function() {
//     ctx.drawImage(player, 20, 300, canvas.width, canvas.height)
// }

// player.onerror = function() {
//     console.log('Ошибка загрузки изображения!')
// }


ctx.beginPath();
ctx.arc(250, 250, 100, 0, Math.PI * 2, true);
ctx.fillStyle = 'yellow';
ctx.fill();
ctx.stroke();
ctx.closePath();

ctx.beginPath();
ctx.arc(210, 220, 10, 0, Math.PI * 2, true);  
ctx.arc(290, 220, 10, 0, Math.PI * 2, true);  
ctx.fillStyle = 'black';
ctx.fill();
ctx.closePath();

ctx.beginPath();
ctx.arc(250, 250, 60, 0, Math.PI, false); 
ctx.stroke();
ctx.closePath();




// ctx.fillStyle = 'green';
// ctx.fillRect(10, 10, 100, 100);

// ctx.strokeStyle = 'red';
// ctx.strokeRect(150, 10, 100, 100);

// ctx.clearRect(20, 20, 30, 30)


// ctx.beginPath();
// ctx.moveTo(350, 10);
// ctx.lineTo(450, 10);
// ctx.lineTo(450, 160);
// ctx.closePath();
// ctx.stroke();

// ctx.beginPath();
// ctx.moveTo(650, 10);
// ctx.lineTo(700, 160);
// ctx.lineTo(800, 160);
// ctx.closePath();
// ctx.fillStyle = 'yellow';
// ctx.fill();

// ctx.fillStyle = 'red';
// ctx.stroke();

// ctx.beginPath();
// ctx.arc(100, 200, 50, 0, Math.PI * 2, true);
// ctx.strokeStyle = 'black';
// ctx.stroke();


// ctx.beginPath();
// ctx.arc(250, 200, 50, 0, Math.PI, true);
// ctx.stroke();
