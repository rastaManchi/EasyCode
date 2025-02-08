

function check(el) {
    let animation_time = parseInt(el.getAttribute('fade-in'))
    let is_vis = el.getAttribute('is_vis')
    let opacity
    if (is_vis === 'true')
        {
            opacity = 1
        } else {
            opacity = 0
        }
        
    let start_anim = Date.now()

    let timer = setInterval(function () {
        el.style.opacity = opacity
        if (Date.now() - start_anim >= animation_time*1000)
        {
            if (is_vis === 'true')
                {
                    el.setAttribute('is_vis', "false")
                } else {
                    el.setAttribute('is_vis', "true")
                }
            clearInterval(timer)
            
        }
        if (is_vis === 'true')
        {
            opacity -= 0.1
        } else {
            opacity += 0.1
        }
        
    }, 100)

}