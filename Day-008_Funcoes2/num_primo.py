# Write your code below this line 👇
def prime_checker(number):
    contador = 0
    for n in range(1, number + 1):
        if number % n == 0:
            contador += 1
        if contador > 2:
            print('Não é primo')
            return
    print('É primo')

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)