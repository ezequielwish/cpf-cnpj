from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/<tipo>')
def generate(tipo):
    if tipo == 'cpf':
        # lógica de geração de CPF
        return jsonify({'value': '123.456.789-00'})
    elif tipo == 'cnpj':
        # lógica de geração de CNPJ
        return jsonify({'value': '12.345.678/0001-99'})
    return jsonify({'error': 'Tipo inválido'}), 400

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    value = data.get('value', '')
    # lógica de validação
    valido = True if value.startswith('1') else False
    return jsonify({'valid': valido})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
