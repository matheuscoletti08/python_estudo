# Faça um Programa que leia três números e mostre o maior deles.
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
if n1 > n2 and n1 > n3:
    print(f"O maior numero é: {n1 :.0f}")
elif n2 > n1 and n2 > n3:
    print(f"O maior numero é: {n2 :.0f}")
else:
    print(f"O maior numero é: {n3 :.0f}")
