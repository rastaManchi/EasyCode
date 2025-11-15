const canvas = document.getElementById("my_game")
const ctx = canvas.getContext('2d')


canvas.width = 400
canvas.height = 400

const tileSize = 40
const levelIndex = 0

const player = {
    x: 1,
    y: 1
}


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
        [1, 1, 1, 1, 1, 'E', 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 'E', 1, 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ],
    [
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        [1, 'E', 'E', 'E', 'E', 'E', 'E', 'E', ''],
    ]

]

function drawLevel() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const level = levels[levelIndex];
    for (let y = 0; y < level.length; y++) {
        for (let x = 0; x < level[y].length; x++) {
            if (level[y][x] === 1) {
                ctx.fillStyle = "black"
                ctx.fillRect(x * tileSize, y * tileSize, tileSize, tileSize);
            }
            if (level[y][x] === 'E') {
                ctx.fillStyle = 'green'
                ctx.fillRect(x * tileSize + tileSize / 4, y * tileSize + tileSize / 4, tileSize / 2, tileSize / 2)
            }
        }
    }
    ctx.fillStyle = 'purple'
    ctx.fillRect(player.x * tileSize, player.y * tileSize, tileSize, tileSize)
}


function movePlayer(dx, dy) {
    const newX = player.x + dx;
    const newY = player.y + dy;
    const level = levels[levelIndex];

    // Проверяем границы
    if (newX < 0 || newX >= level[0].length || newY < 0 || newY >= level.length) {
        return; // Игрок не может выйти за пределы уровня
    }

    // Проверяем, является ли целевая клетка стеной
    if (level[newY][newX] === 1) {
        return; // Игрок не может пройти через стену
    }

    player.x = newX;
    player.y = newY;

    // Проверка на выход
    if (level[newY][newX] === 'E') {
        levelIndex++; // Переход к следующему уровню
        resetPlayerPosition(); // Сброс позиции игрока на стартовую
    }

    checkGameOver(); // Проверяем, выиграл ли игрок
    drawLevel(); // Обновляем уровень
}

document.addEventListener('keydown', (event) => {
    switch(event.key) {
        case 'ArrowUp':
            movePlayer(0, -1);
            break;
        case 'ArrowDown':
            movePlayer(0, 1)
            break;
        case 'ArrowLeft':
            movePlayer(-1, 0)
            break
        case 'ArrowRight':
            movePlayer(1, 0)
            break
    }
})

drawLevel()