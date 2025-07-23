from flask import Flask, render_template, request, jsonify
from documents_tool import generator, validator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate/<tipo>", methods=["GET"])
def generate(tipo):
    new_document = generator.generate_document(tipo)
    return jsonify({"value": new_document})


@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    document_number = data.get("value", "")
    validation_result = validator.validate_document(document_number)
    print(validation_result)
    return jsonify({"valid": validation_result})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
