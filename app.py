import datetime
import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
import historico

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    data = request.get_json()
    pergunta = data.get("pergunta")

    if not pergunta:
        return jsonify({"erro": "Pergunta não fornecida"}), 400

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pergunta}],
    )

    mensagem = resposta.choices[0].message["content"]

    historico.salvar(pergunta, mensagem)

    return jsonify({"resposta": mensagem})
