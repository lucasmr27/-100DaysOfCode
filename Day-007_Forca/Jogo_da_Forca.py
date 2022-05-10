import random
from enforcado_art import estagio
from palavras_forca import lista_de_palavras



# Escolhendo uma palavra aleatoriamente
palavra_escolhida = random.choice(lista_de_palavras)
vida = 6

# Criando lista com lacunas
display = []
palpites_anteriores = []
for letra in palavra_escolhida:
    display.append('_')
print(estagio[vida],' '.join(display))

fim_de_jogo = False
# Solicitando letra para o jogador
while not fim_de_jogo:
    palpite = input('Digite uma letra: ').lower()
    while palpite in palpites_anteriores:
        palpite = input(f'A letra {palpite} já foi dita, digite outra: ').lower()
    palpites_anteriores.append(palpite)
    # Checando a letra e substituindo lacunas
    for posicao in range(len(palavra_escolhida)):
        if palpite == palavra_escolhida[posicao]:
            display[posicao] = palpite
    # Verificando palpite errado e reduzindo a vida
    if not palpite in display:
        vida -= 1
    # Exibindo informacoes
    print(estagio[vida],'\n'+' '.join(display), "\n("+', '.join(palpites_anteriores)+")")
    # Condicoes de vitoria ou derrota
    if vida == 0:
        fim_de_jogo = True
        print('Você perdeu!!!')
    if '_' not in display:
        fim_de_jogo = True
        print('Parabéns, você venceu!!!')

