const canvas = document.getElementById("my_game")
const ctx = canvas.getContext('2d')
let x = 0, dx = 0
const speed = 2
let enemy_x = 100
let enemy_y = 0


function animate() {
    ctx.clearRect(0, 0, 800, 800)
    ctx.fillStyle = 'red'
    ctx.fillRect(enemy_x, enemy_y, 30, 30)
    ctx.fillStyle = 'green'
    ctx.fillRect(x, 0, 30, 30)
    x += dx
    check_collision()
    requestAnimationFrame(animate)
}

function keyDownHandler(event) {
    if (event.key == 'ArrowRight') {
        dx = speed
    }
    else if (event.key == 'ArrowLeft') {
        dx = -speed
    }
}

function keyUpHandler(event) {
    if (event.key == 'ArrowRight' || event.key == 'ArrowLeft') {
        dx = 0
    }
}

function check_collision() {
    if (x < enemy_x + 30 && x + 30 > enemy_x) {
        console.log('Столкновение')
    }
}

document.addEventListener('keydown', keyDownHandler)
document.addEventListener('keyup', keyUpHandler)


animate()

