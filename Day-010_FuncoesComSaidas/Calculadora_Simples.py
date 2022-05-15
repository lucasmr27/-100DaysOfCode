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
for operacao in operacoes:
    print(operacao)

proxima = True
while proxima:
    simbolo_da_operacao = input("Qual operação deseja realizar?")
    num2 = int(input('Digite o próxima número?'))
    calculo = operacoes[simbolo_da_operacao]
    resposta = calculo(num1, num2)
    print(f"{num1} {simbolo_da_operacao} {num2} = {resposta}")
    if input(f'Digite "s" para continuar calculando com {resposta}, ou digite "n" para finalizar.') == 's':
        num1 = resposta
    else:
        proxima = False

