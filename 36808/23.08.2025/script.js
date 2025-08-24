const btn = document.getElementById("floatingButton")
const modal = document.querySelector(".modal")
const close_modal = document.querySelector(".close")

btn.addEventListener('click', () => {
    modal.style.display = "block"
})

close_modal.addEventListener('click', function() {
    modal.style.display = "none"
})