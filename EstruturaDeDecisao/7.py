# Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f"o maior numero é: {n1 :.0f}")
elif n2 > n1 and n2 > n3:
    print(f"o maior numero é: {n2 :.0f}")
else: 
    print(f"o maior numero é: {n3 :.0f}")

if n1 < n2 and n1 < n3:
    print(f"o menor numero é: {n1 :.0f}")
elif n2 < n1 and n2 < n3:
    print(f"o menor numero é: {n2 :.0f}")
else: 
    print(f"o menor numero é: {n3 :.0f}")