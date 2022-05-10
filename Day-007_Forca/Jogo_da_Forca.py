import random


lista_de_palavras = ['arvore', 'carro', 'camelo', 'cigarro', 'apartamento', 'mochila']

# Escolhendo uma palavra aleatoriamente
palavra_escolhida = random.choice(lista_de_palavras)

# Testando o jogo
print(palavra_escolhida)

# Criando lista com lacunas
display = []
for letra in palavra_escolhida:
    display.append('_')
print(display)

fim_de_jogo = False
# Solicitando letra para o jogador
while not fim_de_jogo:
    palpite = input('Digite uma letra: ').lower()
    # Checando a letra e substituindo lacunas
    for posicao in range(len(palavra_escolhida)):
        if palpite == palavra_escolhida[posicao]:
            display[posicao] = palpite
    print(display)

    if '_' not in display:
        fim_de_jogo = True
        print('Parabéns, você venceu!!!')

