from flask import Flask, request, render_template, redirect, url_for, flash
from models import db, Agendamento
from config import Config
from datetime import datetime
from sqlalchemy import func

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    client_filter = request.args.get('client')
    servico_filter = request.args.get('servico')
    data_filter = request.args.get('data')
    

    agendamentos = Agendamento.query

    if client_filter:
        agendamentos = agendamentos.filter(Agendamento.client.like(f"%{client_filter}%"))
    
    if servico_filter:
        agendamentos = agendamentos.filter(Agendamento.servico.like(f"%{servico_filter}%"))
    
    if data_filter:
        try:
            data_formatada = datetime.strptime(data_filter, "%d-%m-%Y").strftime("%d-%m-%Y")

            for agendamento in agendamentos:
                agendamentos = [
                    ag for ag in agendamentos if ag.data.strip() == data_formatada
                ]
        except ValueError:
            flash('A data deve estar no formato DD-MM-YYYY', 'danger')
            return redirect(url_for('index'))
    return render_template('index.html', agendamentos=agendamentos)

@app.route('/agendamentos/create', methods=['GET', 'POST'])
def create_agendamento():
    if request.method == 'POST':
        data = request.form['data']
        horario = request.form['horario']
        client = request.form['client']
        servico = request.form['servico']

        try:
            data_formatada = datetime.strptime(data, "%d-%m-%Y").strftime("%d-%m-%Y")
        except ValueError:
            flash('A data deve estar no formato DD-MM-YYYY', 'danger')
            return redirect(url_for('create_agendamento'))

        novo_agendamento = Agendamento(data=data_formatada, horario=horario, client=client, servico=servico)

        db.session.add(novo_agendamento)
        db.session.commit()
        flash('Agendamento criado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/agendamentos/update', methods=['GET', 'POST'])
@app.route('/agendamentos/update/<int:id>', methods=['GET', 'POST'])
def update_agendamento(id=None):
    agendamento = None

    if id:
        agendamento = Agendamento.query.get(id)
        if not agendamento:
            flash('Agendamento não encontrado', 'danger')
            return redirect(url_for('index'))

    if request.method == 'POST':
        agendamento_id = request.form.get('agendamento_id')
        if agendamento_id:
            agendamento = Agendamento.query.get(agendamento_id)
            if not agendamento:
                flash('Agendamento não encontrado', 'danger')
                return redirect(url_for('update_agendamento'))

        if agendamento:
            data = request.form.get('data')
            if not data:
                flash('O campo "data" é obrigatório!', 'danger')
                return redirect(url_for('update_agendamento', id=agendamento.id))

            horario = request.form.get('horario')
            client = request.form.get('client')
            servico = request.form.get('servico')

            try:
                data_formatada = datetime.strptime(data, "%d-%m-%Y").strftime("%d-%m-%Y")
            except ValueError:
                flash('A data deve estar no formato DD-MM-YYYY', 'danger')
                return redirect(url_for('update_agendamento', id=agendamento.id))

            agendamento.data = data_formatada
            agendamento.horario = horario
            agendamento.client = client
            agendamento.servico = servico

            db.session.commit()
            flash('Agendamento salvo com sucesso!', 'success')
            return redirect(url_for('index'))

    return render_template('update.html', agendamento=agendamento)

@app.route('/agendamentos/delete/<int:id>', methods=['POST'])
def delete_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    db.session.delete(agendamento)
    db.session.commit()
    flash('Agendamento deletado com sucesso!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)   