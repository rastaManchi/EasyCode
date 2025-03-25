let lessons = {}

function addLesson(id, name) {
    if (!lessons[id]) {
        lessons[id] = name
        console.log('Урок добавлен')
    }
    else {
        console.log('Такой урок существует!')
    }
}

function delLesson(id) {
    if (lessons[id]) {
        delete lessons[id]
        console.log(`Курс с ID ${id} удален`)
    }
    else {
        console.log(`Курс с ID ${id} не найден!`)
    }
}

function listLessons() {
    console.log('Список всех уроков')
    for (let lessonID in lessons) {
        console.log(`ID: ${lessonID}, Название: ${lessons[lessonID]}`)
    }
}

addLesson(1, 'JS')
addLesson(101, 'Python')
addLesson(103, 'CSS')
addLesson(1, "C++")
listLessons()
delLesson(103)
listLessons()