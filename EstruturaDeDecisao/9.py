<<<<<<< HEAD
# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

lista = [n1, n2, n3]

ordenado = sorted(lista, reverse=True)

print("numero em ordem decrescente: ")
for num in ordenado:
=======
# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

lista = [n1, n2, n3]

ordenado = sorted(lista, reverse=True)

print("numero em ordem decrescente: ")
for num in ordenado:
>>>>>>> 41fcc7c66e9c7e7e2f0b092ba21870cdf69d8b8d
    print(num)