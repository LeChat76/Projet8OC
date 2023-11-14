// background-script.js

$(document).ready(function() {
    var bgImage = $(".background-image");
  
    // Définir la position de l'image de manière aléatoire
    function randomPosition() {
      var xPos = Math.random() * 100;
      var yPos = Math.random() * 100;
      bgImage.css("background-position", xPos + "% " + yPos + "%");
    }
  
    // Appeler la fonction pour définir la position initiale
    randomPosition();
  
    // Appeler la fonction à chaque redimensionnement de la fenêtre
    $(window).resize(randomPosition);
  });
  