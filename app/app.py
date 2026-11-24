
import os
import mysql.connector
from flask import Flask

app = Flask(__name__)


def menu():
    return """
    <nav style="background:#222; padding:15px; text-align:center;">
        <a href="/" style="color:white; margin:15px;">Início</a>
        <a href="/sobre" style="color:white; margin:15px;">Sobre</a>
        <a href="/contato" style="color:white; margin:15px;">Contato</a>
        <a href="/alunos" style="color:white; margin:15px;">Alunos</a>
    </nav>
    """


def conectar_banco():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )


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
        <p>Esta aplicação foi desenvolvida utilizando Python, Flask,
        MySQL, Apache e Docker.</p>
        <p>O objetivo é demonstrar a integração entre uma aplicação web,
        um banco de dados e um servidor HTTP em containers.</p>
    </div>
    """


@app.route("/contato")
def contato():
    return menu() + """
    <div style="background:#fef9e7; padding:40px; text-align:center;">
        <h1>Contato</h1>
        <p>Aplicação acadêmica desenvolvida para a disciplina de
        Redes e Administração de Sistemas.</p>
        <p>Instituto Federal de São Paulo - Campus Campos do Jordão.</p>
    </div>
    """


@app.route("/alunos")
@app.route("/aluno")
def alunos():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("SELECT id, nome FROM alunos ORDER BY id")
        registros = cursor.fetchall()

        html = menu()
        html += """
        <div style="background:#f4ecf7; padding:40px; text-align:center;">
            <h1>Alunos cadastrados no MySQL</h1>
            <ul style="list-style:none; padding:0;">
        """

        for aluno in registros:
            html += f"<li>{aluno['id']} - {aluno['nome']}</li>"

        html += """
            </ul>
            <p>Dados consultados diretamente no banco de dados MySQL.</p>
        </div>
        """

        return html

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
