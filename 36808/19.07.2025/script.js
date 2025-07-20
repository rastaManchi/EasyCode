const canvas = document.getElementById('game')
const ctx = canvas.getContext('2d')

let dx = 2
let dy = 2
let x = 0
let y = 0

const img = new Image()
img.src = 'Exclude.png'

function drawPlayer() {
    ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight)
    x += dx
    y += dy
    ctx.drawImage(img, x, y)
}


function animate() {
    drawPlayer()
    requestAnimationFrame(animate)
}

img.onload = animate()