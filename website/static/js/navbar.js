/*
const scriptPhosphorIcons = document.createElement('script');
scriptPhosphorIcons.src = 'https://unpkg.com/@phosphor-icons/web';
document.head.appendChild(scriptPhosphorIcons);

let navbar = document.querySelector('.navbar');

function createNavbar(){
  const srcImages = {
    home: '',
    Tools: '',
    Blast: '',
    Jbrowse: '',
    Download: '',
    About: '',
  };

  const contentNavbar = `
    <div class='menuIcon'>
      <div class='menuBar1'></div>
      <div class='menuBar2'></div>
      <div class='menuBar3'></div>
    </div>
    <a class="tdbLogo" onclick="redirectPage(this)">
      <figure>
        <img src='../static/icons/database_icon.svg' alt="Ícone do Theobroma DataBase" />
      </figure>
      <h2>TDB</h2>
    </a>
    <ul class='navbarTools'>
      <li>
        <a href="/index.html">
          <img src='../static/icons/home_fill_icon.svg' alt="Ícone de início" />
          Home
        </a>
      </li>
      <li>
        <span class='toolsBttn'>
          <img src='../static/icons/tools_icon.svg' alt="Ícone de ferramentas" />
          Tools
        </span>
        <div class='dropDown'>
          <a href="/blast">
            <img src='../static/icons/genetic_icon.svg' alt="BLAST tool icon " />
            BLAST
          </a>
          <a href="/jbrowse">
            <img src='../static/icons/genetic_icon.svg' alt="JBROWSE tool icon" />
            JBROWSE
          </a>
          <a href="/clustalw">
            <img src='../static/icons/genetic_icon.svg' alt="CLUSTAL tool icon" />
            CLUSTALW
          </a>
		  <a href="/tree">
            <img src='../static/icons/genetic_icon.svg' alt="TREE tool icon" />
           FiloTree
          </a>
        </div>
      </li>
      <li>
        <a href="/download">
          <img src="../static/icons/download_icon.svg" alt="Ícone de download" />
          Download
        </a>
      </li>
      <li>
        <a href="/about">
          <img src='../static/icons/info_icon.svg' alt="Ícone de informações" />
          About
        </a>
      </li>
    </ul>
    <div class='searchBttn'>
      <form >
        <button class="btn btn-primary" type="submit" value="Search" data-target="search-engine">
          <i class="ph-bold ph-magnifying-glass"></i>
        </button>
       
        
        
        <input class="form-control" data-target="Search-page" type="text" name="search_input" placeholder="Search Gene/Genome" aria-label="Search Gene/Genome/Function">
      </form>
    </div>
  `;

  navbar.innerHTML = contentNavbar;
};

// class="form-inline" method="POST" id="form-search" action="/search_engine"

createNavbar();

*/


const menuButton = document.querySelector('.menuButton');
const navbarTools = document.querySelector('.navbarTools');

menuButton.addEventListener('click', () => {
	menuButton.classList.toggle('animate');
	navbarTools.classList.toggle('showNavbar');
});