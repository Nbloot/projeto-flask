
from flask import Flask

app = Flask(__name__)

def menu():
    return """
    <nav style="background:#222; padding:15px; text-align:center;">
        <a href="/" style="color:white; margin:15px;">Início</a>
        <a href="/sobre" style="color:white; margin:15px;">Sobre</a>
        <a href="/contato" style="color:white; margin:15px;">Contato</a>
        <a href="/aluno" style="color:white; margin:15px;">Aluno</a>
    </nav>
    """

@app.route("/")
def inicio():
    return menu() + """
    <div style="background:#eaf2f8; padding:40px; text-align:center;">
        <h1>Bem-vindo ao Flask no Docker!</h1>
        <p>Aplicação desenvolvida para o trabalho de RASI.</p>
    </div>
    """

@app.route("/sobre")
def sobre():
    return menu() + """
    <div style="background:#e8f8f5; padding:40px; text-align:center;">
        <h1>Sobre o Projeto</h1>
        <p>Esta aplicação foi desenvolvida utilizando Python, Flask e Docker.</p>
        <p>O objetivo é demonstrar a criação e execução de uma aplicação web em um container.</p>
    </div>
    """

@app.route("/contato")
def contato():
    return menu() + """
    <div style="background:#fef9e7; padding:40px; text-align:center;">
        <h1>Contato</h1>
        <p>Aplicação acadêmica desenvolvida para a disciplina de Redes e Administração de Sistemas.</p>
        <p>Instituto Federal de São Paulo - Campus Campos do Jordão.</p>
    </div>
    """

@app.route("/aluno")
def aluno():
    return menu() + """
    <div style="background:#f4ecf7; padding:40px; text-align:center;">
        <h1>Informações do Aluno</h1>
        <p>Aluno: Nicolas Elias Bloot</p>
	<p>Aluno: Victor Amorim Vieira Cirillo da Silva
        <p>Curso: Técnico em Informática</p>
        <p>Disciplina: Redes e Administração de Sistemas (RASI)</p>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
