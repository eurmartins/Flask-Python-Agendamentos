import unittest
from app import app, db
from models import Agendamento

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_ctx = app.app_context()
        self.app_ctx.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all() 
        self.app_ctx.pop() 

    def test_create_agendamento(self):
        response = self.app.post('/agendamentos/create', data={
            'data': '01-05-2025',
            'horario': '14:00',
            'client': 'John Doe',
            'servico': 'Corte de Cabelo'
        })
        self.assertEqual(response.status_code, 302)

    def test_create_agendamento_invalid_date(self):
        response = self.app.post('/agendamentos/create', data={
            'data': '01/05/2025',
            'horario': '14:00',
            'client': 'Jane Doe',
            'servico': 'Corte de Cabelo'
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_agendamento(self):
        agendamento = Agendamento(data='01-05-2025', horario='14:00', client='John Doe', servico='Corte de Cabelo')
        db.session.add(agendamento)
        db.session.commit()

        response = self.app.post(f'/agendamentos/delete/{agendamento.id}')
        self.assertEqual(response.status_code, 302)

    def test_update_agendamento(self):
        agendamento = Agendamento(data='01-05-2025', horario='14:00', client='John Doe', servico='Corte de Cabelo')
        db.session.add(agendamento)
        db.session.commit()

        response = self.app.post(f'/agendamentos/update/{agendamento.id}', data={
            'data': '02-05-2025',
            'horario': '15:00',
            'client': 'John Doe',
            'servico': 'Corte de Cabelo'
        })
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
