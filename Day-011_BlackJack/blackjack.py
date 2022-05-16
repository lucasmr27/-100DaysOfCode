from art import logo
import random

lista_de_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pegar_carta(cartas):
    """Adiciona uma carta aleatória na lista de cartas da mão"""
    cartas.append(random.choice(lista_de_cartas))


def contar_pontos(cartas):
    pontos = 0
    for posicao in range(len(cartas)):
        pontos = sum(cartas)
        if pontos <= 21:
            return pontos
        elif cartas[posicao] == 11:
            cartas[posicao] = 1
            pontos = contar_pontos(cartas)
    return pontos


def vez_jogador(continuar=True):
    while continuar:
        pegar_carta(jogador)
        pontos = contar_pontos(jogador)
        print(f"Suas cartas são: [{']['.join([str(x)for x in jogador])}], você tem {pontos} pontos.")
        if pontos > 21:
            return False
        continuar = input("Aperte 's' para pegar outra carta ou 'n' para passar. ").lower() == "s"
    return True


def vez_dealer(pontos_jogador):
    pontos_dealer = contar_pontos(dealer)
    print(f"As cartas do Dealer são: [{']['.join([str(x)for x in dealer])}], ele tem {pontos_dealer} pontos.")
    while pontos_jogador > pontos_dealer:
        pegar_carta(dealer)
        pontos_dealer = contar_pontos(dealer)
        print(f"As cartas do Dealer são: [{']['.join([str(x)for x in dealer])}], ele tem {pontos_dealer} pontos.")
        if pontos_dealer > 21:
            return True
    return False


novo_jogo = True
while novo_jogo:
    print(logo)

    jogador = []
    pegar_carta(jogador)
    dealer = []
    pegar_carta(dealer)
    pegar_carta(dealer)
    print(f"Cartas do Dealer são: [{dealer[0]}][?]")
    venceu = vez_jogador()
    if venceu:
        venceu = vez_dealer(contar_pontos(jogador))

    if contar_pontos(jogador) == contar_pontos(dealer):
        print("O jogo empatou")
    elif venceu:
        print("Você ganhou!")
    else:
        print("Você perdeu")
    novo_jogo = input("Deseja jogar novamente? Digite sim ou não. ").lower() == 'sim'
