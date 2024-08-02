<<<<<<< HEAD
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso do peixe: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"A quantidade deu excedida, e vc precisará pagar {multa:.0f} reais")
else:
=======
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso do peixe: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"A quantidade deu excedida, e vc precisará pagar {multa:.0f} reais")
else:
>>>>>>> 41fcc7c66e9c7e7e2f0b092ba21870cdf69d8b8d
    print(f"ta tudo certo caba, pode levar tranquilo 💋")