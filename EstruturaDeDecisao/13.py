# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_semana = int(input("Qual o numero correspondente ao dia da semana?: "))

if dia_semana == 1:
        print("Domingo")

elif dia_semana == 2:
        print("Segunda")

elif dia_semana == 3:
        print("Terça")

elif dia_semana == 4:
        print("Quarta")

elif dia_semana == 5:
        print("Quinta")

elif dia_semana == 6:
        print("Sexta")

elif dia_semana == 7:
        print("Sabado")

else:
        print("Valor invalido")