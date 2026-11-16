
# Aplicação Flask com Docker

## 1. Sobre o projeto

Este projeto foi desenvolvido como atividade da disciplina de Redes e Administração de Sistemas (RASI), do curso Técnico em Informática do Instituto Federal de São Paulo – Campus Campos do Jordão.

O objetivo é desenvolver e executar uma aplicação web utilizando Python, Flask e Docker.

## 2. Tecnologias utilizadas

- Python 3.14
- Flask
- Docker
- HTML e CSS
- Ubuntu Server

## 3. Funcionalidades

A aplicação possui quatro páginas:

- **Início (/):** página principal da aplicação.
- **Sobre (/sobre):** apresenta informações sobre o projeto.
- **Contato (/contato):** apresenta informações institucionais.
- **Aluno (/aluno):** apresenta informações acadêmicas do aluno.

## 4. Estrutura do projeto

```text
projeto-flask/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
└── README.md
```

## 5. Como executar o projeto

### Construir a imagem Docker

```bash
docker build -t flask-app .
```

### Executar o container

```bash
docker run -d -p 5000:5000 --name meu-flask flask-app
```

### Verificar o funcionamento

```bash
docker ps
```

### Consultar os registros

```bash
docker logs meu-flask
```

## 6. Acessar a aplicação

Com o container em execução, acesse pelo navegador:

- http://localhost:5000/
- http://localhost:5000/sobre
- http://localhost:5000/contato
- http://localhost:5000/aluno

O endereço `localhost` é utilizado no computador hospedeiro quando a porta 5000 está encaminhada para a máquina virtual.

## 7. Autores

Nicolas Elias Bloot
Victor Amorim Vieira Cirillo da Silva

Curso Técnico em Informática  
Instituto Federal de São Paulo – Campus Campos do Jordão  
Disciplina: Redes e Administração de Sistemas (RASI)
