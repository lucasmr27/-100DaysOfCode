#Password Generator Project
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao gerador de senhas!")
num_letras= int(input("Digite a quantidade de letras!\n"))
num_simbolos = int(input(f"Digite a quantidade de símbolos!\n"))
num_numeros = int(input(f"Digite a quantidade de números!\n"))

for _ in range(5):
    senha_lista = [random.choice(letras) for i in range(num_letras)] \
                  + [random.choice(simbolos) for item in range(num_simbolos)] \
                  + [random.choice(numeros) for num in range(num_numeros)]
    senha = ''
    random.shuffle(senha_lista)
    for char in senha_lista:
        senha += char
    print(senha)
