import random
import art
from data import data
import os


def limpar():
    """ Limpa a tela do terminal """
    os.system('clear' if os.name == 'posix' else 'cls')


def compare(a):
    global option_a
    b = random.randint(0, len(data) - 1)
    option_a = b
    print(f'Compare A: {data[a]["name"]}, {data[a]["description"]}, from {data[a]["country"]}.')
    print(art.vs)
    print(f'Against B: {data[b]["name"]}, {data[b]["description"]}, from {data[b]["country"]}.')
    if input('Who has more followers? Type "A" or "B": ').upper() == 'A':
        return data[a]['follower_count'] > data[b]['follower_count']
    else:
        return data[a]['follower_count'] < data[b]['follower_count']


option_a = random.randint(0, len(data) - 1)
score = 0
print(art.logo)
while True:
    if compare(option_a):
        score += 1
        limpar()
        print(art.logo)
        print(f"You're right! Current score: {score}")
        continue
    else:
        limpar()
        print(f"Sorry, that's wrong. Final score: {score}")
    break
