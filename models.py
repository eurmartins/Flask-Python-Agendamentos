from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Agendamento(db.Model):
    __tablename__ = 'agendamento'
    id = db.Column(db.Integer, primary_key=True)
    _data = db.Column("data", db.String(10))
    horario = db.Column(db.String(5))  
    client = db.Column(db.String(100))
    servico = db.Column(db.String(100))

    def __repr__(self):
        return f'<Agendamento {self.id}>'

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        try:
            if isinstance(value, str):
                self._data = datetime.strptime(value, "%d-%m-%Y").strftime("%d-%m-%Y")
            else:
                self._data = value.strftime("%d-%m-%Y")
        except ValueError:
            raise ValueError("A data deve estar no formato DD-MM-YYYY")
