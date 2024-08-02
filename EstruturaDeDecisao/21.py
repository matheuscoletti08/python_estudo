# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = float(input("Qual o valor de saque?: "))
if valor_saque > 10 and valor_saque < 600:
        notas_100 = valor_saque // 100
        valor_saque = valor_saque % 100
        notas_50 = valor_saque // 50
        valor_saque = valor_saque % 50
        notas_10 = valor_saque // 10
        valor_saque = valor_saque % 10
        notas_5 = valor_saque // 5
        valor_saque = valor_saque % 5
        notas_1 = valor_saque // 1
        valor_saque = valor_saque % 1
else:
        print("Valor inválido")

print(f"{notas_100:.0f} notas de 100, {notas_50:.0f} notas de 50, {notas_10:.0f} notas de 10, {notas_5:.0f} notas de 5 e {notas_1:.0f} notas de 1: ")
