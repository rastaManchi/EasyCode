document.getElementById('generate').addEventListener('click', generatePassword)


function generatePassword() {
    const length = parseInt(document.getElementById('length').value);
    const language = document.getElementById('language').value;
    const complexity = document.getElementById('complexity').value;

    let charset = '';

    if (language === 'en') {
        if (complexity === 'simple') {
            charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
        } else if (complexity === 'medium') {
            charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        } else {
            charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+[]{}|;:,.<>?';
        }
    } else if (language === 'ru') {
        if (complexity === 'simple') {
            charset = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя';
        } else if (complexity === 'medium') {
            charset = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789';
        } else {
            charset = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789!@#$%^&*()_+[]{}|;:,.<>?';
        }
    }

    let password = '';
    let i = 0;

    while (i < length) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
        i++;
    }

    document.getElementById('password').textContent = password;
}







