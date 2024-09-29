// script.js

const fileInput = document.getElementById('fileInput');
const preview = document.getElementById('preview');

fileInput.addEventListener('change', function() {
    const file = this.files[0]; // Obtém o arquivo selecionado

    if (file) {
        const reader = new FileReader(); // Cria um novo FileReader

        reader.onload = function(event) {
            preview.src = event.target.result; // Define o src da imagem para o resultado
            preview.style.display = 'block'; // Mostra a imagem
        }

        reader.readAsDataURL(file); // Lê o arquivo como URL
    }
});
