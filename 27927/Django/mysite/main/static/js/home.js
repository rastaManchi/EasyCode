const form = document.getElementById('add_form')
const tasks = document.getElementById('tasks')


form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = e["srcElement"].querySelectorAll('input')
    const csrf_token = data[0].value
    const task_name = data[1].value
    const task_text = document.getElementById('task_text').value
    let form = new FormData()
    form.append('csrfmiddlewaretoken', csrf_token)
    form.append('task_name', task_name)
    form.append('task_text', task_text)
    fetch('/add/', {
        method: 'POST',
        body: form
    })
    .then(response => {
        return response.json()
    })
    .then(from_server => {
        if (from_server.status) {
            const new_task_div = document.createElement('div')

            const new_task_header = document.createElement('h3')
            new_task_header.textContent = task_name

            const new_task_text = document.createElement('p')
            new_task_text.textContent = task_text

            new_task_div.appendChild(new_task_header)
            new_task_div.appendChild(new_task_text)

            tasks.appendChild(new_task_div)
        }
        data[1].value = "" 
        document.getElementById('task_text').value = ""
    })
})