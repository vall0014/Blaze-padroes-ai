from flask import Flask, request, render_template_string
from historico import analisar_padroes

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Analisador de Cores</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background-color: #111; color: white; }
        textarea { width: 100%; height: 100px; margin-top: 10px; }
        .resultado { margin-top: 20px; white-space: pre-wrap; background-color: #222; padding: 15px; border-radius: 8px; }
        .botao { margin-top: 10px; padding: 10px 20px; background-color: #444; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Analisador de Padrões de Cores</h1>
    <form method="post">
        <label for="historico">Cole o histórico de cores (ex: vermelho, preto, branco...):</label>
        <textarea name="historico" required>{{ historico }}</textarea><br>
        <button class="botao" type="submit">Analisar</button>
    </form>
    {% if resultado %}
        <div class="resultado">{{ resultado }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    historico = ""

    if request.method == "POST":
        historico = request.form["historico"]
        resultado = analisar_padroes(historico)

    return render_template_string(HTML_TEMPLATE, resultado=resultado, historico=historico)

if __name__ == "__main__":
    app.run(debug=True)
