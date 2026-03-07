const inputSearch = document.getElementById("inputSearch")
const butSearch = document.getElementById("butSearch")
const postBlock = document.getElementById("postBlock")



butSearch.addEventListener("click",() => {
    let form = new FormData() 
    form.append(
        "Text", inputSearch.value   
    )
    fetch("/Search/", {
        method:"POST",
        body:form
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        postBlock.innerHTML = ""
        for (post of data) {
            let li_elem = document.createElement("li")
            let h3_elem = document.createElement("h3")
            let p_elem = document.createElement("p")
            h3_elem.textContent = post[1]
            p_elem.textContent = post[2]
            li_elem.appendChild(h3_elem)
            li_elem.appendChild(p_elem)
            postBlock.appendChild(li_elem)
        }
    })
})