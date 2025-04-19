let tasks = []


function addTask() {
    const taskInput = document.getElementById('taskInput')
    const task = taskInput.value.trim()
    alert(task)
    if (task) {
        tasks.push(task)
        taskInput.value = ""
        renderTasks()
    }
}


function renderTasks() {
    const taskList = document.getElementById('taskList')
    taskList.innerHTML = ''
    tasks.forEach((task, index) => {
        const li = document.createElement('li')
        li.textContent = task
        const deleteButton = document.createElement('button')
        deleteButton.textContent = 'Delete'
        deleteButton.onclick = () => {
            deleteTask(index)
        }
        li.appendChild(deleteButton)
        taskList.appendChild(li)
    })
}