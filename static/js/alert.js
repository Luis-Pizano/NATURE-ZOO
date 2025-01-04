// Función para cerrar las alertas al hacer clic en la "X"
document.addEventListener("DOMContentLoaded", function () {
    // Obtener todos los botones de cierre dentro de las alertas
    const closeButtons = document.querySelectorAll('.alert .btn-close');
    
    // Añadir un evento de clic a cada botón de cierre
    closeButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            // Prevenir la propagación del evento si es necesario
            event.stopPropagation();
            
            // Encontrar el contenedor de la alerta
            const alertBox = button.closest('.alert');
            // Remover la alerta del DOM
            alertBox.style.display = 'none';
        });
    });
});
