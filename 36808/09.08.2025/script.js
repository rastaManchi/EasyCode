const canvas = document.getElementById("Game")
const ctx = canvas.getContext('2d')

let tile_height = 20
let tile_width = 20

lvl1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, "S", 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "F", 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

function drawLevel() {
    let row_count = 0;
    for (let row of lvl1) {
        let column_count = 0;
        for (let column of row) {
            if (column == 1) {
                ctx.fillStyle = "black"
                ctx.fillRect(column_count * tile_width, row_count * tile_height, tile_width, tile_height)
            }
            else if (column == "S") {
                ctx.fillStyle = "green"
                ctx.fillRect(column_count * tile_width, row_count * tile_height, tile_width, tile_height)
            }
            else if (column == "F") {
                ctx.fillStyle = "red"
                ctx.fillRect(column_count * tile_width, row_count * tile_height, tile_width, tile_height)
            }
            column_count++
        }
        row_count++
    }
}

function animate() {
    drawLevel()
    requestAnimationFrame(animate)
}

animate()