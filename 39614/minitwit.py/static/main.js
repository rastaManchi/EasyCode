const search_input = document.getElementById('search_input')
const search_btn = document.getElementById('search_btn')
const posts_list = document.getElementById('posts_list')


search_btn.addEventListener('click', () => {
    if (search_input.value.trim() != '') {
        posts_list.innerHTML = ""

        form = new FormData()
        form.append('search_text', search_input.value.trim())

        fetch('/search_posts', {
            method: 'POST',
            body: form
        })
        .then(response => {
            return response.json()
        })
        .then(data => {
            data.forEach(element => {
                // li_element = document.createElement('li')
                // h2_element = document.createElement('h2')
                // p_element = document.createElement('p')
                // h2_element.textContent = element[1]
                // p_element.textContent = element[2]
                
                // li_element.appendChild(h2_element)
                // li_element.appendChild(p_element)

                // posts_list.appendChild(li_element)
                console.log(element)
                posts_list.innerHTML = `
                    <li>
                        <h2>${element[1]}</h2>
                        <p>${element[2]}</p>
                    </li>
                `
            });
        })
    }
})
