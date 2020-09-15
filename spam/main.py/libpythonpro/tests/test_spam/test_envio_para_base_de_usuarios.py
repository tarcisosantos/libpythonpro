from libpythonpro.spam.enviador_de_email import Enviador


def test_envio_de_spam():
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'bentessantostarciso@gmail.com',
        'Curso Python Pro',
        'Confira os Módulos fantásticos'
    )