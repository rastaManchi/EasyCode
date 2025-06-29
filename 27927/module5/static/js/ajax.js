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
        success: function () {
            $(`.tr_${user_id}`).remove()
        }
    })
})

$('.edit_btn').click(function () {
    alert(`Изменить - user_id = ${this.getAttribute('user_id')}`)
})


$('#login_change').click(function () {
    const user_id = $(this).attr('user_id')
    const new_login = $("#login").val()
    $.ajax({
        url: '/change',
        type: 'UPDATE',
        contentType: "application/json",
        data: JSON.stringify({
            event: "change_login",
            user_id: user_id,
            new_data: new_login
        }),
        success: function () {
            alert('Логин изменен')
            $(".current_name").text(new_login)
        }
    })
})

$('#email_change').click(function () {
    const user_id = $(this).attr('user_id')
    const new_email = $("#email").val()
    $.ajax({
        url: '/change',
        type: 'UPDATE',
        contentType: "application/json",
        data: JSON.stringify({
            event: "change_email",
            user_id: user_id,
            new_data: new_email
        }),
        success: function () {
            alert('Почта изменена')
            $(".current_email").text(new_email)
        }
    })
})

