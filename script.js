// Get the modal
var card_modal = document.getElementById("modal");

// Get the button that opens the modal
var botao_modal_1 = document.getElementById("botao_modal_1");
var botao_modal_2 = document.getElementById("botao_modal_2");
var botao_modal_3 = document.getElementById("botao_modal_3");

// Get the <span> element that closes the modal
var voltar = document.getElementsByClassName("modal_baixo_botao_voltar")[0];

var sim = document.getElementsByClassName("modal_baixo_botao_sim")[0];

// When the user clicks the button, open the modal 
botao_modal_1.onclick = function() {
    card_modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
voltar.onclick = function() {
    card_modal.style.display = "none";
};

sim.onclick = function() {
    card_modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    card_modal.style.display = "none";
  };
};