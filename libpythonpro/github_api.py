import requests


def buscar_avatar(usuario):
    """
    Buscar o avatar de um usuário no Github
    :param usuario: str como o nome do usuário no github
    :return: str vok o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
