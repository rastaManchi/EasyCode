const btn = document.getElementById('btn')
const btn2 = document.querySelector('#btn')

const items = document.querySelectorAll('.item')
console.log(items[1])

btn.addEventListener('click', function () {
    alert('Hi')
})

btn.textContent = 'Что-то там'
items[1].innerHTML = '<h1>Привет</h1>'

btn.style.backgroundColor = 'red'

const new_element = document.createElement('button')
new_element.textContent = 'Купить'
items[0].appendChild(new_element)


alert(btn2.getAttribute('id'))
items[2].setAttribute('is_new', '100')
items[3].removeAttribute('class')

btn.remove()

items[4].classList.add('new_class')
items[4].classList.remove('old_class')
items[4].classList.toggle('class')
console.log(items[4].classList.contains('new_class'))