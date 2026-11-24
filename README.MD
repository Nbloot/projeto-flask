# Aplicação Flask com Docker Compose

## 1. Sobre o projeto

Este projeto foi desenvolvido como atividade da disciplina de Redes e Administração de Sistemas (RASI), do curso Técnico em Informática do Instituto Federal de São Paulo – Campus Campos do Jordão.

O objetivo é desenvolver e executar uma aplicação web utilizando Python, Flask e Docker, evoluindo de um container individual para uma arquitetura com múltiplos serviços integrados por meio do Docker Compose.

A aplicação utiliza um banco de dados MySQL para armazenar informações dos alunos e um servidor Apache para receber as requisições HTTP e encaminhá-las à aplicação Flask.

**Repositório:** https://github.com/Nbloot/projeto-flask

## 2. Tecnologias utilizadas

- Python 3.14-slim
- Flask 3.1.2
- MySQL 8.0
- Apache HTTP Server 2.4
- Docker
- Docker Compose
- HTML e CSS
- Ubuntu Server

## 3. Arquitetura do projeto

O ambiente é composto por três serviços:

- **db:** container responsável pelo banco de dados MySQL, utilizando um volume persistente para armazenar os dados.
- **flask:** container responsável pela aplicação web desenvolvida em Python com Flask. A comunicação com o MySQL é realizada por meio de variáveis de ambiente.
- **server:** container com Apache HTTP Server, configurado como proxy reverso para encaminhar as requisições à aplicação Flask.

O Docker Compose gerencia a inicialização e a comunicação entre os três serviços.

## 4. Funcionalidades

A aplicação possui as seguintes páginas:

- **Início (/):** página principal da aplicação.
- **Sobre (/sobre):** apresenta informações sobre o projeto e as tecnologias utilizadas.
- **Contato (/contato):** apresenta informações institucionais.
- **Alunos (/alunos):** consulta e apresenta os registros cadastrados na tabela `alunos` do banco de dados MySQL.

A rota `/aluno` também está disponível como endereço alternativo para a página de alunos.

## 5. Estrutura do projeto

```text
projeto-flask/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── compose.yaml
├── .env
├── .gitignore
├── httpd.conf
└── README.MD
```

O arquivo `.env` armazena as credenciais utilizadas pelos serviços. Ele é protegido pelo `.gitignore` e não deve ser enviado ao GitHub.

## 6. Configuração e execução

### 6.1. Configurar as variáveis de ambiente

Na raiz do projeto, crie o arquivo `.env` com as seguintes variáveis:

```env
MYSQL_ROOT_PASSWORD=sua_senha_root
MYSQL_PASSWORD=sua_senha_flask
```

As senhas devem corresponder às credenciais configuradas no banco de dados.

### 6.2. Construir e iniciar os serviços

Execute o comando:

```bash
docker compose up -d --build
```

Esse comando constrói a imagem da aplicação Flask, quando necessário, e inicia os três serviços em segundo plano.

### 6.3. Verificar os containers

Para verificar o estado dos serviços, execute:

```bash
docker compose ps
```

Para consultar os registros de execução:

```bash
docker compose logs
```

### 6.4. Criar a tabela de alunos

Após a inicialização do MySQL, acesse o banco de dados:

```bash
docker compose exec db mysql -u root -p
```

Informe a senha definida em `MYSQL_ROOT_PASSWORD` no arquivo `.env`.

Em seguida, execute os comandos SQL:

```sql
USE meu_banco;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

INSERT INTO alunos (nome)
VALUES
('Nicolas Elias Bloot'),
('Victor Amorim Vieira Cirillo da Silva');
```

A tabela será utilizada pela aplicação para apresentar os registros na página de alunos.

**Observação:** execute a criação da tabela apenas uma vez em um banco que ainda não possua essa estrutura.

## 7. Acesso à aplicação

Com os serviços em execução, a aplicação pode ser acessada pelo navegador.

No ambiente configurado com encaminhamento de porta NAT:

- http://localhost:8080/
- http://localhost:8080/sobre
- http://localhost:8080/contato
- http://localhost:8080/alunos

O Apache recebe as requisições pela porta 80 da máquina virtual e as encaminha ao container Flask, que utiliza a porta 5000 internamente.

## 8. Persistência dos dados

O serviço MySQL utiliza o volume Docker `mysql_data`, responsável por manter os dados armazenados mesmo quando os containers são parados ou recriados.

Para interromper os serviços sem remover o volume de dados, utilize:

```bash
docker compose down
```

Para iniciar novamente:

```bash
docker compose up -d
```

## 9. Autores

**Nicolas Elias Bloot**

**Victor Amorim Vieira Cirillo da Silva**

Curso Técnico em Informática

Instituto Federal de São Paulo – Campus Campos do Jordão

Disciplina: Redes e Administração de Sistemas (RASI)
