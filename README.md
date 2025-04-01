
# Flask Python Agendamentos

Este é um projeto simples de agendamentos utilizando Flask, Python, e SQLite como banco de dados. Ele permite a criação, leitura, atualização e exclusão de agendamentos através de uma API RESTful. O projeto utiliza SQLAlchemy como ORM e Flask-Migrate para gerenciar migrações de banco de dados.

## 📋 Requisitos

Antes de começar, você precisa ter o Python instalado em sua máquina:

- **Link para instalar o Python**: [Python Downloads](https://www.python.org/downloads/)

Após a instalação você pode verificar a versão do Python com o seguinte comando:
```bash
python --version
```

Além disso, é necessário instalar algumas dependências:

- Flask
- Flask-SQLAlchemy
- Flask-Migrate

## 🛠️ Instalação

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/eurmartins/Flask-Python-Agendamentos.git
cd Flask-Python-Agendamentos
```

Instale as dependências do projeto:

```bash
pip install flask
pip install flask_sqlalchemy
pip install flask_migrate
```
## 🚀 Rodando o Projeto

Após a configuração do banco de dados, você pode rodar o servidor Flask com o seguinte comando:

```bash
py app.py
```

O servidor estará rodando em `http://127.0.0.1:5000/`.

## ⚙️ Funcionalidades

- **POST** `/agendamentos`: Criação de um novo agendamento.
- **GET** `/agendamentos`: Listar todos os agendamentos.
- **PUT** `/agendamentos/<id>`: Atualizar um agendamento existente.
- **DELETE** `/agendamentos/<id>`: Excluir um agendamento.

## 🧪 Testes Unitários
```
python -m unittest test_app.py
```

## 🤝 Contribuindo
Sinta-se à vontade para enviar contribuições! Para isso, faça um fork do repositório, crie uma branch com sua funcionalidade, e envie um pull request.

## Agradecimento
Muito Obrigado pelo desafio e pela oportunidade TimeSaver!


## Contatos 

email: victormartinssantos.work@gmail.com

linkedin: https://www.linkedin.com/in/victormartinssantos/
