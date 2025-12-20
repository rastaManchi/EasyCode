const search_value = document.getElementById('search_value')
const search_btn = document.getElementById('search_btn')
const posts_block = document.getElementById('posts')


function start_search() {
    if (search_value.value.length != 0) {
        fetch('/search/', {
            method: 'POST',
            body: JSON.stringify({'txt': search_value.value})
        })
        .then(response => {
            return response.json()
        })
        .then(data => {
            posts_block.innerHTML = data.text
        })
    }
}


search_btn.addEventListener('click', start_search)