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

// Pegar o menu de hamburguer e as opções do menu
hamburguer = document.querySelector(".navbar_hamburguer");
menu = document.querySelector(".navbar_menu");

// Quando clicar no menu de hamburguer, ganhará uma classe chamada "showing", 
// e enquanto o menu de hamburguer ter essa classe as opções aparecerão
// Se clicar denovo (para fechar), fecha as opções do menu e tira a classe "showing" do menu de hamburguer.
hamburguer.onclick = function() {
  menu.style.display = 'flex';
  menu.classList.toggle("showing");
  if (menu.classList.contains("showing")) {
    menu.style.display = 'none';
  }

}