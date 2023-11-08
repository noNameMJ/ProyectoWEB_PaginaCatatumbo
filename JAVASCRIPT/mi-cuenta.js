document.addEventListener("DOMContentLoaded", function () {
    // Comprobar si hay una sesión iniciada en el almacenamiento local
    const usuarioSesion = JSON.parse(localStorage.getItem("usuarioSesion"));

    // Obtener elementos del DOM que necesitas modificar
    const perfilDiv = document.getElementById("perfil");
    const nombreUsuario = document.getElementById("nombre-usuario");
    const iniciarSesionButton = document.getElementById("iniciar-sesion-button");
    const registroButton = document.getElementById("registro-button");
    const inicioSesionForm = document.getElementById("inicio-sesion-form");
    const registroForm = document.getElementById("registro-form");


    if (usuarioSesion) {
        // Si hay una sesión iniciada, mostrar el perfil del usuario
        perfilDiv.style.display = "block";
        iniciarSesionButton.style.display = "none";
        registroButton.style.display = "none";

        // Mostrar información del usuario
        nombreUsuario.textContent = "Nombre: " + usuarioSesion.nombre;
        // Puedes agregar más detalles del perfil aquí
    } else {
        // Si no hay una sesión iniciada, mostrar opciones de inicio de sesión y registro
        perfilDiv.style.display = "none";
        iniciarSesionButton.style.display = "block";
        registroButton.style.display = "block";

        // Manejar eventos de inicio de sesión y registro
        iniciarSesionButton.addEventListener("click", function () {
            inicioSesionForm.style.display = "block";
            registroForm.style.display = "none";
        });

        registroButton.addEventListener("click", function () {
            inicioSesionForm.style.display = "none";
            registroForm.style.display = "block";
        });
    }
});

function iniciarSesion(correo, contrasena) {
    fetch('../usuarios.json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Error al cargar el archivo JSON');
    }
    return response.json();
  })
  .then(data => {
  
    const usuarios = data.usuarios;
    
    const usuario = usuarios.find((u) => u.correo === correo && u.contrasena === contrasena);
  
    if (usuario) {
      // Usuario autenticado, almacena la información en localStorage
      localStorage.setItem("usuarioAutenticado", JSON.stringify(usuario));
      return true;
    } else {
      alert('Error');
      return false; // Autenticación fallida
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });

    
}