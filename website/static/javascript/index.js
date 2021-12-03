const burgerIcon = document.querySelector('#burger')
const navbarMenu = document.querySelector('#nav-links')

burgerIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active')
})

const tabs = document.querySelectorAll('.navbar-menu a')
const tabContent = document.querySelectorAll('#tab-content > div')

//prepara a adição do jbrowse em "browse-page"
const jbTab = document.getElementById('somewhere-else')
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
                if (target === "somewhere-else") {
                    jbTab.appendChild(iframe)
                }
            }
        })
    })
})

//atualiza nome de arquivo no formulário do Blast
const camposArquivo = document.querySelectorAll('.file.has-name')
camposArquivo.forEach((campo) => {
    const entradaArquivo = campo.querySelector('.file-input')
    const nome = campo.querySelector('.file-name')
    entradaArquivo.addEventListener('change', () => {
        const arquivos = entradaArquivo.files
        if (arquivos.length === 0) {
            nome.innerText = 'Nenhum Arquivo Selecionado'
        } else {
            nome.innerText = arquivos[0].name
        }
    })
})
const forms = document.getElementsByTagName('form')
for (const form of forms) {
    form.addEventListener('reset', () => {
        const nomes = form.querySelectorAll('.file-name')
        nomes.forEach((nome) => {
            nome.innerText = 'Nenhum Arquivo Selecionado'
        })
    })
}
