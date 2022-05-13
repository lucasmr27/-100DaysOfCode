from art import logo
import os


print(logo)
print("Welcome to the secret auction program.")
again = True
bidders = {}
while again:
    name = input("What is your name? ")
    bid = float(input("What's your bid? R$"))
    bidders[name] = bid
    if input("Are there any other bidders? Type 'yes' or 'no'.").lower() == 'no':
        again = False
    # Comando para limpar a tela sendo clear em linux ou mac e cls no windows
    os.system('clear' if os.name == 'posix' else 'cls')
bigger_bid = 0
winner = ''
for person in bidders:
    if bidders[person] > bigger_bid:
        bigger_bid = bidders[person]
        winner = person
print(f"The winner is {winner} with a bid of R${bidders[winner]}.")
