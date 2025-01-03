function togglePassword() {
    const passwordInput = document.getElementById('password'); // input password con id = password
    const toggleIcon = document.getElementById('toggle-password'); //icono con id = toggle-password
    
    // Cambiar el tipo de input entre 'password' y 'text'
    if (passwordInput.type === 'password') { // Al hacer click si el input es de tipo password entonces lo transforma tipo text
        passwordInput.type = 'text'; // Mostrar contraseña
        toggleIcon.classList.remove('fa-eye-slash');
        toggleIcon.classList.add('fa-eye');
    } else {
        passwordInput.type = 'password'; // Ocultar contraseña
        toggleIcon.classList.remove('fa-eye');
        toggleIcon.classList.add('fa-eye-slash');
    }
}
