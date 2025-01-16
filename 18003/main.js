const btn = document.getElementById('btn');
const btn2 = document.querySelector('#btn');
const parent1 = document.getElementsByClassName('parent')[0];
const parent2 = document.querySelector('.parent');
const parent3 = document.querySelectorAll('.parent')[0];

parent2.innerHTML = '<b>Привет</b>';
btn.textContent = 'Не кнопка';
let element = document.createElement('p');
parent1.appendChild(element)

btn2.remove()

parent3.style.display = 'none';

let attr = parent1.getAttribute('abc');
console.log(attr);

parent1.setAttribute('abcd', 'Привет Мир')
parent1.removeAttribute('abc');

parent2.classList.contains