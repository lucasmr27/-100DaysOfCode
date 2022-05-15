from art import logo


# Add
def soma(n1, n2):
    return n1 + n2


# Subtract
def subtracao(n1, n2):
    return n1 - n2


# Multiply
def multiplicacao(n1, n2):
    return n1 * n2


# Divide
def divisao(n1, n2):
    return n1 / n2


operacoes = {
    '+': soma,
    '-': subtracao,
    '*': multiplicacao,
    '/': divisao
}
num1 = int(input('Qual é o primeiro número?'))
num2 = int(input('Qual é o segundo número?'))

for operacao in operacoes:
    print(operacoes[operacao](num1, num2))

