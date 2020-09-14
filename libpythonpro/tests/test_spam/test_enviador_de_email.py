import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not  None

@pytest.mark.parametrize(
    'destinatario',
    ['tarcisosantos@meta.edu.br', 'bentessantostarciso@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'sgdo1@hotmail.com',
        'Teste de Programação Python3',
        'Exemplo de spam com python curso Python Pro 2020.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'bentessantostarciso']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'sgdo1@hotmail.com',
            'Teste de Programação Python3',
            'Exemplo de spam com python curso Python Pro 2020.'
        )

