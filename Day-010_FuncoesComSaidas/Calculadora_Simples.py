from art import logo
import os


def limpar():
    """ Limpa a tela do terminal """
    os.system('clear' if os.name == 'posix' else 'cls')


def soma(n1, n2):
    """Realiza a soma dos dois termos"""
    return n1 + n2


# Subtract
def subtracao(n1, n2):
    """Realiza a subtração dos dois termos"""
    return n1 - n2


# Multiply
def multiplicacao(n1, n2):
    """Realiza a multiplicação dos dois termos"""
    return n1 * n2


# Divide
def divisao(n1, n2):
    """Realiza a divisão dos dois termos"""
    if n1 == 0:
        return "Valor impossível ou indeterminado!"
    return n1 / n2


operacoes = {
    '+': soma,
    '-': subtracao,
    '*': multiplicacao,
    '/': divisao
}


def calculadora():
    limpar()

    print(logo)

    num1 = float(input('Qual é o primeiro número?'))
    for operacao in operacoes:
        print(operacao)
    proxima = True

    while proxima:
        simbolo_da_operacao = input("Qual operação deseja realizar?")
        num2 = float(input('Digite o próxima número?'))
        calculo = operacoes[simbolo_da_operacao]
        resposta = calculo(num1, num2)

        print(f"{num1} {simbolo_da_operacao} {num2} = {resposta}")
        if isinstance(resposta, str):
            input('Pressione enter para iniciar um novo calculo.')
            calculadora()
            proxima = False
            continue
        if input(f'Digite "s" para continuar calculando com {resposta},'
                 f' ou digite "n" para iniciar uma nova operação.') == 's':
            num1 = resposta
        else:
            proxima = False
            calculadora()


calculadora()
