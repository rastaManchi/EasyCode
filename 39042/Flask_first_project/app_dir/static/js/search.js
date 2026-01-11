const search_value = document.getElementById('search_value')
const search_btn = document.getElementById('search_btn')
const posts_block = document.getElementById('posts')


function start_search() {
    if (search_value.value.length != 0) {
        posts_block.innerHTML = ""
        const my_form = new FormData()
        my_form.append('txt', search_value.value)
        fetch('/search/', {
            method: 'POST',
            body: my_form
        })
        .then(response => {
            return response.json() // [ [1, title, content, author] ]
        })
        .then(data => {
            console.log(data)
            for (let post of data) { 
                const li_elem = document.createElement('li')
                const h2_elem = document.createElement('h2')
                h2_elem.textContent = post[1]
                const p_elem = document.createElement('p')
                p_elem.textContent = post[2]
                const author_elem = document.createElement('p')
                author_elem.textContent = post[3]
                li_elem.appendChild(h2_elem)
                li_elem.appendChild(p_elem)
                li_elem.appendChild(author_elem)
                posts_block.appendChild(li_elem)
            }
        })
    }

    else {
        window.location.reload()
    }
}


search_btn.addEventListener('click', start_search)