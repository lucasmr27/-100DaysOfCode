print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo a ilha do tesouro!")
print("Sua missão é achar o tesouro!")
escolha1 = input('você encontrou um cruzamento para onde deseja ir? Digite "esquerda" ou "direita?" ').lower()
if escolha1 == "esquerda":
    escolha2 = input('Você encontrou um lago. Há uma ilha no meio do lago.'
                     'Digite "esperar" para esperar um barco ou digite "nadar" para ir nadando. ').lower()
    if escolha2 == "esperar":
        escolha3 = input("Você chega a ilha ileso. Há uma casa com 3 portas. Uma Vermelha, uma azul e uma amarela."
                         "Qual cor você escolhe? ").lower()
        if escolha3 == "amarela" or escolha3 == "amarelo":
            print("Parabens você encontrou o tesouro!!! Você venceu!!!")
        elif escolha3 == "vermelho" or escolha3 == "vermelha":
            print("A sala se incendiou! Você Perdeu!")
        else:
            print("Você foi devorado por demônios! Você perdeu!")
    else:
        print("O lago está cheio de piranhas! Você perdeu!")
else:
    print("Você caiu em um buraco! Você perdeu")
