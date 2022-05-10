import random


lista_de_palavras = ['arvore', 'carro', 'camelo', 'cigarro', 'apartamento', 'mochila']

# Escolhendo uma palavra aleatoriamente
palavra_escolhida = random.choice(lista_de_palavras)

# Testando o jogo
print(palavra_escolhida)

# Solicitando letra para o jogador
palpite = input('Digite uma letra: ').lower()

# Checando a letra
for letra in (palavra_escolhida):
    if palpite == letra:
        print(letra)
    else:
        print('-')