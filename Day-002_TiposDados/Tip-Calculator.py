print("Bem-vindo à calculadora de gorjetas!")
total = float(input("Qual é o total da conta? R$"))
gorjeta = float(input("Qual a porcentagem de gorjeta você gostaria de pagar? "))/100
num_pessoas = int(input("Com quantas pessoas será divida a conta? "))
total_por_pessoa = round(total * (1 + gorjeta) / num_pessoas, 2)
print(f"Cada pessoa terá que pagar R${total_por_pessoa}")
