<<<<<<< HEAD
# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# 1 - par ou ímpar;
# 2 - positivo ou negativo;
# 3 - inteiro ou decimal.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

escolha = float(input("Qual opçao vc quer? (1, 2 ou 3): "))

if escolha == 1:
    if numero1 % 2 == 0 and numero2 % 2 == 0:
        print("Os numeros sao pares")
    elif numero1 % 2 == 0 and numero2 % 2 != 0:
        print("O primeiro numero é par e o segundo é impar")
    elif numero1 % 2 != 0 and numero2 % 2 == 0:
        print("O primeiro numero é impar e o segundo é par")
    else:
        print("Os numeros sao impares")

elif escolha == 2:
    if numero1 > 0 and numero2 > 0:
        print("Os dois numeros sao positivos")
    elif numero1 > 0 and numero2 < 0:
        print("O primeiro numero é positivo e o segundo é negativo")
    elif numero1 < 0 and numero2 > 0:
        print("O primeiro numero é negativo e o segundo é positivo")
    else:
        print("Os numeros sao negativos")

elif escolha == 3:
    if numero1 % 1 == 0 and numero2 % 1 == 0:
        print("Os numeros sao inteiros")
    elif numero1 % 1 == 0 and numero2 % 1 != 0:
        print("O primeiro numero é inteiro e o segundo é decimal")
    elif numero1 % 1 != 0 and numero2 % 1 == 0:
        print("O primeiro numero é decimal e o segundo é inteiro")
    else:
        print("Os numeros sao decimais")

else:
=======
# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# 1 - par ou ímpar;
# 2 - positivo ou negativo;
# 3 - inteiro ou decimal.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

escolha = float(input("Qual opçao vc quer? (1, 2 ou 3): "))

if escolha == 1:
    if numero1 % 2 == 0 and numero2 % 2 == 0:
        print("Os numeros sao pares")
    elif numero1 % 2 == 0 and numero2 % 2 != 0:
        print("O primeiro numero é par e o segundo é impar")
    elif numero1 % 2 != 0 and numero2 % 2 == 0:
        print("O primeiro numero é impar e o segundo é par")
    else:
        print("Os numeros sao impares")

elif escolha == 2:
    if numero1 > 0 and numero2 > 0:
        print("Os dois numeros sao positivos")
    elif numero1 > 0 and numero2 < 0:
        print("O primeiro numero é positivo e o segundo é negativo")
    elif numero1 < 0 and numero2 > 0:
        print("O primeiro numero é negativo e o segundo é positivo")
    else:
        print("Os numeros sao negativos")

elif escolha == 3:
    if numero1 % 1 == 0 and numero2 % 1 == 0:
        print("Os numeros sao inteiros")
    elif numero1 % 1 == 0 and numero2 % 1 != 0:
        print("O primeiro numero é inteiro e o segundo é decimal")
    elif numero1 % 1 != 0 and numero2 % 1 == 0:
        print("O primeiro numero é decimal e o segundo é inteiro")
    else:
        print("Os numeros sao decimais")

else:
>>>>>>> 41fcc7c66e9c7e7e2f0b092ba21870cdf69d8b8d
    print("Opção invalida")