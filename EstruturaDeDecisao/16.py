# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

a_valor = float(input("Digite o valor de A: "))
b_valor = float(input("Digite o valor de B: "))
c_valor = float(input("Digite o valor de C: "))
delta = (b_valor**2) - 4*a_valor*c_valor

if a_valor == 0:
        print("A equação não é do segundo grau")
elif delta < 0:
        print("A equação não possui raizes reais")
elif delta > 0:
        x1 = (-b_valor + math.sqrt(delta)) / (2*a_valor)
        x2 = (-b_valor - math.sqrt(delta)) / (2*a_valor)
        print(f"A equação possui duas raizes reais: {x1} e {x2}")
elif delta == 0:
        x = -b_valor / (2*a_valor)
        print(f"A equação possui apenas uma raiz real: {x}")

