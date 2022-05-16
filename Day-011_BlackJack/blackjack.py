from art import logo
import random

lista_de_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)


def pegar_carta(cartas):
    """Adiciona uma carta aleatória na lista de cartas da mão"""
    cartas.append(random.choice(lista_de_cartas))


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


jogador = []
pegar_carta(jogador)
dealer = []
pegar_carta(dealer)
pegar_carta(dealer)
continuar = True


while continuar:
    pegar_carta(jogador)
    print(f"Suas cartas são: {jogador}, você tem {contar_pontos(jogador)} pontos.")
    if contar_pontos(jogador) > 21:
        print("você perdeu")
        break
    continuar = input("Aperte 's' para pegar outra carta ou 'n' para passar.") == "s"

print(f"As cartas do Dealer são: {dealer}, ele tem {contar_pontos(dealer)} pontos.")
