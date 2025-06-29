const button = document.getElementById('btn')


button.addEventListener('mouseenter', () => {
    button.style.backgroundColor = 'red'
    button.textContent = '<img src="x" onerror="alert(1)">'
})
button.addEventListener('mouseleave', () => {
    button.style.backgroundColor = 'white'
})

