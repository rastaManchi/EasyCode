let name = "Булат";
let surname = "Закиров";
const greeting = 'Привет';
const test_button = document.getElementById("test")
const login_input = document.getElementById('login')


test_button.addEventListener("click", () => {
    console.log(greeting + ', ' + name + " " + surname)
    console.log(test_button.textContent.trim())
    console.log(login_input.value)
})


// console.log(greeting + ', ' + name + " " + surname)

