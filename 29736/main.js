const canvas = document.getElementById('gameCanvas')
const ctx = canvas.getContext('2d')


const tileSize = 40

const levels = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 'E', 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 'E', 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
]


function drawLevel() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    const level = levels[0]
    for (let y = 0; y < level.length; y++) {
        for (let x = 0; x < level[y].length; x++) {
            if (level[y][x] === 1) {
                ctx.fillStyle = 'black'
                ctx.fillRect(x*tileSize, y*tileSize, tileSize, tileSize)
            }
            if (level[y][x] === 'E') {
                ctx.fillStyle = 'green'
                ctx.fillRect(x*tileSize + tileSize/4, y*tileSize + tileSize/4, tileSize/2, tileSize/2)
            }
        }
    }
}

drawLevel()

