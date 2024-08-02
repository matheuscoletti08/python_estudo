# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

n = 1
while n > 0:
    number = int(input("coloque um numero de 0 a 10: "))

    if number <= 10:
        print("o numero é aceito")
    else:
        print("o numero não é aceito")
