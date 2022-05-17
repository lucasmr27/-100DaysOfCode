import os


def limpar():
    """ Limpa a tela do terminal """
    os.system('clear' if os.name == 'posix' else 'cls')
