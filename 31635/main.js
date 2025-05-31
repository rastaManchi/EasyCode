const canvas = document.getElementById("game")
const ctx = canvas.getContext('2d')

canvas.width = 400
canvas.height = 400
const tilesize = 40


const player = {
    x: 1,
    x: 1
}


const levels = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 'E', 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 'E', 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
    ]
]

let indexLevel = 0

function drawLevel() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    const level = levels[indexLevel]
    for (let y = 0; y < level.length; y++) {
        for (let x = 0; x<level[y].length; x++) {
            if (level[y][x] == 1) {
                ctx.fillStyle = 'black'
                ctx.fillRect(x * tilesize, y * tilesize, tilesize, tilesize)
            }
            if (level[y][x] == 'E') {
                ctx.fillStyle = 'green'
                ctx.fillRect(x * tilesize + tilesize/4, y * tilesize + tilesize / 4, tilesize / 2, tilesize / 2)
            }
        }
    }
}

// function drawPlayer() {}

function movePlayer(dx, dy) {
    const newX = player.x + dx
    const newY = player.y + dy
    const level = levels[indexLevel]

    if (newX < 0 || newX >= level[0].length || newY < 0 || newY >= level.length) {
        return
    }

    if (level[newY][newX] == 1) {
        return
    }

    player.x = newX
    player.y = newY

    if (level[newY][newX] == 'E') {
        indexLevel++
        // resetPlayerPosition()
    }

    // checkGameOver()

    // drawPlayer()
    drawLevel()
}


// function animate() {}