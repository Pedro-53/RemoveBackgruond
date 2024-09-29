from flask import Flask, request, send_file, render_template
import rembg
from io import BytesIO
import os

app = Flask(__name__)

# Rota principal renderizando o arquivo index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return "No image uploaded", 400

    #declarando o file
    file = request.files['image']

    # Verificar o tipo MIME da imagem
    if file.mimetype not in ['image/jpeg', 'image/jpg', 'image/png']:
        return "Invalid image type. Only JPEG, PNG, and JPG are allowed.", 400

    input_image = file.read()
    output_image = rembg.remove(input_image)

    # Retornar a imagem sem fundo
    output = BytesIO(output_image)
    output.seek(0)

    fileName, ext = os.path.splitext(file.filename)
    file_extension = "_rmbg.png" #adicionando uma extenção personalizada a imagem
    new_filename = fileName + file_extension
    return send_file(output, mimetype='image/png', as_attachment=True, download_name=new_filename)

if __name__ == '__main__':
    # Rodar o Flask no host 0.0.0.0 para que ele seja acessível externamente
    app.run(debug=True, host="0.0.0.0", port=5000)
