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

edit_avatar_div = document.createElement("div")
edit_avatar_div.style.display = "flex"
edit_avatar_div.style.alignItems = "center"
edit_avatar_input = document.createElement("input")
edit_avatar_input.setAttribute("type","file")
edit_avatar_btn = document.createElement('button')
edit_avatar_btn.textContent = 'Изменить изображение'
edit_avatar_btn.style.color = 'white'
edit_avatar_btn.style.backgroundColor = 'green'
edit_avatar_btn.style.width = '100%'
edit_avatar_btn.style.display = 'flex'
edit_avatar_btn.style.justifyContent = 'center'
edit_avatar_btn.style.padding = '1em'
edit_avatar_btn.style.borderRadius = '15px'
edit_avatar_btn.setAttribute("id","edit_avatar_btn")
edit_avatar_btn.onclick = function(){
            const img =edit_avatar_input.files[0]
            const form_data=new FormData()
            form_data.append("avatar",img)
            fetch("/change_avatar",{
                method:"post",
                body:form_data
            })
            .then(response=>{
                location.reload()
            })
        }

