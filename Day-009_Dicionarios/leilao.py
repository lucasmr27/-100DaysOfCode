from art import logo


print(logo)
print("Welcome to the secret auction program.")
again = True
while again:
    name = input("What is your name?")
    bid = input("What's your bid?")
    if input("Are there any other bidders? Type 'yes' or 'no'.").lower() == 'no':
        again = False

