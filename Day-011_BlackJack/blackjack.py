from art import logo
import random

lista_de_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)


def pegar_carta():
    return random.choice(lista_de_cartas)


def contar_pontos(cartas):
    pontos = int()
    for posicao in range(len(cartas)):
        pontos = sum(cartas)
        if pontos <= 21:
            return pontos
        elif cartas[posicao] == 11:
            cartas[posicao] = 1
            contar_pontos(cartas)
    return pontos


cartas_jogador = []
cartas_dealer = []
