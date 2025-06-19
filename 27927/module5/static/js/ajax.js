// const search_btn = document.querySelector('.search_btn')
// search_btn.addEventListener('click', () => {
//     fetch('/ajax', {
//         method: "post",
//         body: JSON.stringify({ 'name': 'Булат' })
//     })
//     .then(response => {
//         return response.json()
//     })
//     .then(data => {
//         console.log(data)
//     })
// })

$('.search_btn').click(function () {
    $.ajax({
        url: '/ajax',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({ name: 'Булат' }),
        success: function (response) {
            console.log(response)
        }
    })
})


$('.delete_btn').click(function () {
    let user_id = this.getAttribute('user_id')
    $.ajax({
        url: "/admin",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify(
            {
                event: "delete",
                user_id: user_id
            }
        ),
        success: function() {
            $(`.tr_${user_id}`).remove()
        }        
    })
})

$('.edit_btn').click(function () {
    alert(`Изменить - user_id = ${this.getAttribute('user_id')}`)
})