from flask import Flask, render_template, request, jsonify
from documents_tool import generator, validator

app = Flask(__name__)


@app.route("/")
def index():
    """Renderiza a página inicial."""
    return render_template("index.html")


@app.route("/generate/<tipo>", methods=["GET"])
def generate(tipo):
    """
    Gera um novo documento com base no tipo fornecido.

    Args:
        tipo (str): Tipo do documento a ser gerado (ex: 'cpf', 'cnpj').

    Returns:
        JSON: Documento gerado no formato {"value": "<documento>"}.
    """
    new_document = generator.generate_document(tipo)
    return jsonify({"value": new_document})


@app.route("/validate", methods=["POST"])
def validate():
    """
    Valida um número de documento recebido via JSON.

    Exemplo de entrada:
        { "value": "12345678900" }

    Retorna:
        JSON: Resultado da validação no formato {"valid": True/False}.
    """
    data = request.get_json()
    document_number = data.get("value", "")
    validation_result = validator.validate_document(document_number)
    print(validation_result)
    return jsonify({"valid": validation_result})


if __name__ == "__main__":
    # Executa o servidor Flask em modo debug, acessível na rede local
    app.run(debug=True, host="0.0.0.0")
