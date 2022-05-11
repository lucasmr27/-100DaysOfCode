alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
texto = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    shift_amount = shift_amount % len(alphabet)
    cipher_text = ''
    cipher_alphabet = alphabet[shift_amount: len(alphabet)] + alphabet[0: shift_amount]
    for letra in plain_text:
        cipher_text += cipher_alphabet[alphabet.index(letra)]
    print(cipher_text)


encrypt(texto, shift)
