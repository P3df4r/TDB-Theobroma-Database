const burgerIcon = document.querySelector('#burger')
const navbarMenu = document.querySelector('#nav-links')

burgerIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active')
})

const tabs = document.querySelectorAll('.navbar-menu a')
const tabContent = document.querySelectorAll('#tab-content > div')

tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
        tabs.forEach(item => item.classList.remove('is-active'))
        tab.classList.add('is-active')

        const target = tab.dataset.target
        tabContent.forEach(content => {
            content.classList.add('is-hidden')
            if (content.getAttribute('id') === target) {
                content.classList.remove('is-hidden')
            }
        })
    })
})

