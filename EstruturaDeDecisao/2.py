# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = int(input('Digite um valor: '))

if valor > 0:
    print("esse valor é positivo")
elif valor < 0: 
    print("esse valor é negativo")
else:
    print("esse valor é neutro")
