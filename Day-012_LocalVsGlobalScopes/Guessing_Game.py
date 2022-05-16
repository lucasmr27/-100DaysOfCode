import random
from art import logo


def check_guess(number):
    """Verifica se o palpite está certo, acima ou abaixo do numero secreto"""
    global attempts
    if number < secret_number:
        print('Too low')
    elif number == secret_number:
        print('Congratulation! You win!')
        attempts = 0
    else:
        print('Too high')


play_again = True
while play_again:
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100")

    secret_number = random.randint(1, 100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))
        check_guess(guess)
        attempts -= 1
    if attempts == 0:
        print('You lose!')
    play_again = input('Do you want to play again? "y" or "n"').lower() == 'n'
