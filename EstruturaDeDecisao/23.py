# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
numero = float(input("Digite um numero: "))

if numero % 1 == 0:
        print("O numero é inteiro")

else:
        print("O numero é decimal")