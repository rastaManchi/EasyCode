const canvas = document.getElementById("game")
const ctx = canvas.getContext('2d')


ctx.fillStyle = 'green'
ctx.fillRect(10, 10, 100, 100)

ctx.strokeStyle = 'red'
ctx.strokeRect(150, 10, 100, 100)




// ############################

ctx.clearRect(0, 0, canvas.width, canvas.height)

ctx.fillStyle = 'black'

ctx.beginPath()
ctx.moveTo(50, 50)
ctx.lineTo(200, 50)
ctx.lineTo(125, 200)
ctx.closePath()

ctx.fill()
ctx.stroke()

 // ##################################

ctx.clearRect(0, 0, canvas.width, canvas.height)

ctx.beginPath()
ctx.arc(100, 75, 50, 0, Math.PI, false)
ctx.fill()


 // ####################
ctx.clearRect(0, 0, canvas.width, canvas.height)

ctx.beginPath();
ctx.arc(250, 250, 100, 0, Math.PI * 2, false);
ctx.arc(300, 250, 100, 0, Math.PI, false);
ctx.fillStyle = 'purple';
ctx.fill();
ctx.stroke();

// ################################

ctx.clearRect(0, 0, canvas.width, canvas.height)


const sprite = new Image()
sprite.src = 'wall.jpg'

const sw = 64
const sh = 64


sprite.onload = function () {
    ctx.drawImage(sprite, 0, 0, sw, sh)
}
