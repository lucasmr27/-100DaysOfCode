import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

jokenpo = [rock, paper, scissors, rock, paper]

player = input("O que você escolhe? Pedra, papel ou tesoura?").lower()
if player == 'pedra':
    player = 0
elif player == 'papel':
    player = 1
else:
    player = 2
computer = random.randint(0, 2)
print(f'Você jogou:\n{jokenpo[player]}')
print(f'O computador jogou:\n{jokenpo[computer]}')
if jokenpo[player] == jokenpo[computer]:
    print('O jogo empatou')
elif jokenpo[computer] == jokenpo[player + 1]:
    print('Você perdeu')
else:
    print('Você ganhou')
