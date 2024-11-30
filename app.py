from flask import Flask, render_template, request, redirect, url_for
import pesquisa_storage
import threading

app = Flask(__name__)

# Variável para controlar o status do processamento
status_processing = {"done": False}


@app.route("/", methods=["GET", "POST"])
def index():
    # Resetar o status do processamento ao retornar à página inicial
    status_processing["done"] = False
    if request.method == "POST":
        caminho_principal = request.form.get("caminho_principal")
        caminho_similares = request.form.get("caminho_similares")
        caminho_processados = request.form.get("caminho_processados")

        # Redirecionar para a página de processamento com os parâmetros
        return redirect(
            url_for(
                "process",
                caminho_principal=caminho_principal,
                caminho_similares=caminho_similares,
                caminho_processados=caminho_processados,
            )
        )

    return render_template("index.html")


@app.route("/process", methods=["GET"])
def process():
    caminho_principal = request.args.get("caminho_principal")
    caminho_similares = request.args.get("caminho_similares")
    caminho_processados = request.args.get("caminho_processados")

    # Inicia a função em uma thread separada para não bloquear o navegador
    def run_processing():
        pesquisa_storage.PesquisaStorage(
            caminho_principal, caminho_similares, caminho_processados
        )
        status_processing["done"] = True  # Marcar como concluído

    threading.Thread(target=run_processing).start()

    return render_template("process.html")


@app.route("/check_status", methods=["GET"])
def check_status():
    # Retorna o status do processamento
    if status_processing["done"]:
        return redirect(url_for("complete"))
    return "processing"


@app.route("/complete", methods=["GET"])
def complete():
    return render_template("complete.html")


if __name__ == "__main__":
    app.run(debug=True)
