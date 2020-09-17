
import pytest
from mock import Mock

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


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
        enviador = Mock()
        sessao.salvar(usuario)
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'bentessantostarciso@gmail.com',
        'Curso Python Pro',
        'Estudando as etapas Fantásticas'
    )
    assert len(usuarios) == enviador.enviar.call_count

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Tarciso Santos', email='bentessantostarciso@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tais@gmail.com',
        'Curso Python Pro',
        'Estudando as etapas Fantásticas'
    )
    enviador.enviar.assert_called_once_with(
        'tais@gmail.com',
        'bentessantostarciso@gmail.com',
        'Curso Python Pro',
        'Estudando as etapas Fantásticas'
    )