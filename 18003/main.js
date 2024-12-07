const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

canvas.width = 400;
canvas.height = 400;

let levelindex = 0;
let score = 0;

const tileSize = 40;

const x = 'triger';

let player = {
    x: 1,
    y: 1,
}

let lvls = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, x, 1, 0, 0, 1 ],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
    ],

    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1 ],
        [1, 0, x, 0, 1, 0, 0, 0, 0, 1 ],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
    ]
]


function drawLevel() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const lvl_map = lvls[levelindex]
    for (let y = 0; y < lvl_map.length; y++) {
        for (let x = 0; x < lvl_map[y].length; x++) {
            if (lvl_map[y][x] === 1) {
                ctx.fillStyle = '#000';
                ctx.fillRect(x * tileSize, y * tileSize, tileSize, tileSize);
            }

            else if (lvl_map[y][x] === 'triger') {
                ctx.fillStyle = '#00F';
                ctx.fillRect(x * tileSize, y * tileSize, tileSize, tileSize);
            }
        }
    }

    ctx.fillStyle = "#FFF";
    ctx.font = '20px Arial';
    ctx.fillText('Счет: ' + score, 150, 24);

    ctx.fillStyle = "#F00";
    ctx.fillRect(player.x * tileSize, player.y * tileSize, tileSize, tileSize);
}


function resetPlayerPosition() {
    player.x = 1;
    player.y = 1;
}


function CheeckGameOver() {
    if (levelindex > 1) {
        levelindex = 0;
    }
}


function movePlayer(dx, dy) {
    const newX = player.x + dx;
    const newY = player.y + dy;
    const level = lvls[levelindex];

    if (newX < 0 || newX >= level[0].length || newY < 0 || newY >= level.length) {
        return;
    }

    if (level[newY][newX] === 1) {
        return;
    }

    player.x = newX;
    player.y = newY;

    if (level[newY][newX] === 'triger') {
        levelindex++;
        score += 10;
        resetPlayerPosition();
    }

    CheeckGameOver();
    drawLevel();
}


movePlayer(0, 0)


function keyDownHandler(event) {
    if (event.key === "d" || event.key === "D" || event.key === 'в' || event.key === 'В' || event.key === 'ArrowRight') {
        movePlayer(1, 0);
    } else if (event.key === "a" || event.key === "A" || event.key === 'ф' || event.key === 'Ф' || event.key === 'ArrowLeft') {
        movePlayer(-1, 0);
    } else if (event.key === "w" || event.key === "W" || event.key === 'ц' || event.key === 'Ц' || event.key === 'ArrowUp') {
        movePlayer(0, -1);
    } else if (event.key === "s" || event.key === "S" || event.key === 'ы' || event.key === 'Ы' || event.key === 'ArrowDown') {
        movePlayer(0, 1);
    }
}

document.addEventListener('keydown', keyDownHandler);