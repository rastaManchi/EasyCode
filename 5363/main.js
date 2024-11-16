function test(keyword) {
    const nickname = document.getElementById('nickname').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    user = {
        nickname: nickname,
        email: email,
        password: password,
        keyword: keyword
    }
    console.log(user)
}


test('Тест')






