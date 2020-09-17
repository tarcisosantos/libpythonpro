from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Tarciso Santos', email='bentessantostarciso@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)

def test_listar_usuario(sessao):
     usuarios = [
         Usuario(nome='Tarciso Santos', email='bentessantostarciso@gmail.com'),
         Usuario(nome='Tais Santos', email='tais@gmail.com')
     ]
     for usuario in usuarios:
        sessao.salvar(usuario)
     assert usuarios == sessao.listar()



