# Abre o arquivo e fecha ao concluir os comandos
# o parametro mode determina o que poderá fazer
with open('my_file.txt', mode='r') as file:
    contents = file.read()
    print(contents)


# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()
