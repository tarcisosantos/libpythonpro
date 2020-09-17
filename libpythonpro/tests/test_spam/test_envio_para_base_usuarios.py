import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMork(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados =  0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self. parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados +=1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
          Usuario(nome='Tarciso Santos', email='bentessantostarciso@gmail.com'),
          Usuario(nome='Tais Santos', email='bentessantostarciso@gmail.com')
        ],
        [
            Usuario(nome='Tarciso Santos', email='bentessantostarciso@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        enviador = EnviadorMork()
        sessao.salvar(usuario)
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'bentessantostarciso@gmail.com',
        'Curso Python Pro',
        'Estudando as etapas Fantásticas'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Tarciso Santos', email='bentessantostarciso@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMork()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tais@gmail.com',
        'Curso Python Pro',
        'Estudando as etapas Fantásticas'
    )
    assert enviador.parametros_de_envio == (
        'tais@gmail.com',
        'bentessantostarciso@gmail.com',
        'Curso Python Pro',
        'Estudando as etapas Fantásticas'
    )