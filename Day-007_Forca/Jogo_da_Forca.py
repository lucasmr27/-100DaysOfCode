import random


estagio = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lista_de_palavras = ['arvore', 'carro', 'camelo', 'cigarro', 'apartamento', 'mochila']

# Escolhendo uma palavra aleatoriamente
palavra_escolhida = random.choice(lista_de_palavras)
vida = 6
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
    # Verificando palpite errado e reduzindo a vida
    if not palpite in display:
        vida -= 1
    # Condicoes de vitoria ou derrota
    print(vida,estagio[vida], display)
    if vida == 0:
        fim_de_jogo = True
        print('Você perdeu!!!')
    if '_' not in display:
        fim_de_jogo = True
        print('Parabéns, você venceu!!!')

