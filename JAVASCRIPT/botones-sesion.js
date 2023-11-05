//Script para mostrar u ocultar los formularios
const iniciarSesionButton = document.getElementById("iniciar-sesion-button");
const registroButton = document.getElementById("registro-button");
const inicioSesionForm = document.getElementById("inicio-sesion-form");
const registroForm = document.getElementById("registro-form");
const cancelarButton1 = document.getElementById("cancelar-button1");
const cancelarButton2 = document.getElementById("cancelar-button2");

iniciarSesionButton.addEventListener("click", function() {
    inicioSesionForm.style.display = "block";
    registroForm.style.display = "none";
});

registroButton.addEventListener("click", function() {
    inicioSesionForm.style.display = "none";
    registroForm.style.display = "block";
});

cancelarButton1.addEventListener("click", function(){
    window.location.href="mi-cuenta.html";
});
cancelarButton2.addEventListener("click", function(){
    window.location.href="mi-cuenta.html";
});