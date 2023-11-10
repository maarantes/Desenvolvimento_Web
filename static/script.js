// Variável do modal
var card_modal = document.getElementById("modal");

// Botão que ativa o modal quando clicado
var botao_modal_1 = document.getElementById("botao_modal_1");
var botao_modal_2 = document.getElementById("botao_modal_2");
var botao_modal_3 = document.getElementById("botao_modal_3");

// Botão de voltar que desativa o modal
var voltar = document.getElementsByClassName("modal_baixo_botao_voltar")[0];

var sim = document.getElementsByClassName("modal_baixo_botao_sim")[0];

// Quando clicar no botão, ativar o mo dal
botao_modal_1.onclick = function() {
    card_modal.style.display = "block";
};

// Quando clicar em voltar (ou no sim), desativar o modal
voltar.onclick = function() {
    card_modal.style.display = "none";
};

sim.onclick = function() {
    card_modal.style.display = "none";
};

// Desativar o modal se clicar fora dele
window.onclick = function(event) {
  if (event.target == modal) {
    card_modal.style.display = "none";
  };
};


/* Funcionalidade Menu Hamburguer */

hamburguer = document.querySelector(".navbar_hamburguer");
menu = document.querySelector(".navbar_menu");

//Se apertar o menu ganha a classe showing, se apertar denovo remove a classe showing
hamburguer.onclick = function() {
  menu.style.display = "flex";
  menu.classList.toggle("showing");

}


/* Deixar página ativa em azul no Navbar */

var activePage = window.location.pathname;
let nav_home = document.getElementById("nav_home");
let nav_sobre = document.getElementById("nav_sobre");
let nav_contato = document.getElementById("nav_contato");

if (activePage == "/") {
  nav_home.classList.toggle("active");
}

if (activePage == "/sobre") {
  nav_sobre.classList.toggle("active");
}

if (activePage == "/contato") {
  nav_contato.classList.toggle("active");
}