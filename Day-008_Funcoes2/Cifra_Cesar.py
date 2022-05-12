from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continuar = 'yes'
while continuar == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(plain_text, shift_amount, cipher_direction):
        shift_amount = shift_amount % len(alphabet)
        if cipher_direction == 'decode':
            shift_amount *= -1
        cipher_text = ''
        cipher_alphabet = alphabet[shift_amount: len(alphabet)] + alphabet[0: shift_amount]
        for letra in plain_text:
            if letra in alphabet:
                cipher_text += cipher_alphabet[alphabet.index(letra)]
            else:
                cipher_text += letra
        print(cipher_text)

    caesar(text, shift, direction)
    continuar = input('Deseja reiniciar o programa?').lower()

print('Goodbye!')
