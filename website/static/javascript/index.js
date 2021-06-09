const burgerIcon = document.querySelector('#burger')
const navbarMenu = document.querySelector('#nav-links')

burgerIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active')
})

const tabs = document.querySelectorAll('.navbar-menu a')
const tabContent = document.querySelectorAll('#tab-content > div')

//prepara a adição do jbrowse em "browse-page"
const jbTab = document.getElementById('browse-page')
const iframe = document.createElement('iframe')
iframe.width = "100%"
iframe.height = "750px"
iframe.src = "static/jbrowse/index.html"

tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
        tabs.forEach(item => item.classList.remove('is-active'))
        tab.classList.add('is-active')

        const target = tab.dataset.target
        tabContent.forEach(content => {
            content.classList.add('is-hidden')
            if (content.getAttribute('id') === target) {
                content.classList.remove('is-hidden')
                //toda vez que carrega o jbrowse adiciona ele a "browse-page" vazia
                if (target === "browse-page") {
                    jbTab.appendChild(iframe)
                }
            }
        })
    })
})

