// const element = document.querySelector(".btn")
// const element = document.getElementById('btn')


// element.style.backgroundColor = 'green'
// element.style.border = 'none'
// element.style.padding = '8px'
// element.style.borderRadius = '8px'
// element.style.color = 'white'


// const elements = document.querySelectorAll('#btn')
// elements.forEach((value, index) => {
//     value.style.backgroundColor = `rgb(${Math.random() * (255 - 0 + 1)}, ${Math.random() * (255 - 0 + 1)}, ${Math.random() * (255 - 0 + 1)})`
// })


function add_word() {
    const text = document.getElementById("word").value
    document.querySelector('.result').textContent = text
}


function delme(element) {
    element.remove()
}

function recover(){
    const element = document.createElement('button')
    element.textContent = "удали меня"
    element.onclick = element.remove
    document.body.appendChild(element)
}

const element = document.querySelector('.result')
element.classList.toggle('new')