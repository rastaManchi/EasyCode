function test(keyword) {
    const nickname = document.getElementById('nickname').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    user = {
        nickname: nickname,
        email: email,
        password: password,
        csrf_token: keyword
    }
    console.log(user)
    fetch('/test', {
        method: "POST",
        body: JSON.stringify(user)
    })
}






