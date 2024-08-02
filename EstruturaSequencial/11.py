# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1 - o produto do dobro do primeiro com metade do segundo .
# 2 - a soma do triplo do primeiro com o terceiro.
# 3 - o terceiro elevado ao cubo.

n_float = float(input("Digite um numero real: "))
n1_int = int(input("Digite um numero inteiro: "))
n2_int = int(input("Digite um numero inteiro: "))

res_first = (2 * n_float) + (n1_int/2)
res_second = (3 * n1_int) + n2_int
res_third = (n2_int ** 3)

print(f"{res_first}, {res_second} e {res_third}")