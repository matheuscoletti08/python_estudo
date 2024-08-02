<<<<<<< HEAD
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

ganho_hora = float(input("Digite quanto vc ganha por hora: "))
horas_trabalhadas = float(input("Digite quantas horas vc  trabalha por mes: "))

salario_mes = (ganho_hora * horas_trabalhadas)
imposto_renda = (salario_mes * (11/100) )
inss = (salario_mes * (8/100))
sindicato = (salario_mes * (5/100))
print (f"Salario Bruto: R$ {salario_mes:.2f}")
print (f"Imposto de Renda: R$ {imposto_renda:.2f}")
print (f"INSS: R$ {inss:.2f}")
print (f"Sindicato: R${sindicato:.2f}")
salario_liquido = (salario_mes - imposto_renda - inss - sindicato)
=======
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

ganho_hora = float(input("Digite quanto vc ganha por hora: "))
horas_trabalhadas = float(input("Digite quantas horas vc  trabalha por mes: "))

salario_mes = (ganho_hora * horas_trabalhadas)
imposto_renda = (salario_mes * (11/100) )
inss = (salario_mes * (8/100))
sindicato = (salario_mes * (5/100))
print (f"Salario Bruto: R$ {salario_mes:.2f}")
print (f"Imposto de Renda: R$ {imposto_renda:.2f}")
print (f"INSS: R$ {inss:.2f}")
print (f"Sindicato: R${sindicato:.2f}")
salario_liquido = (salario_mes - imposto_renda - inss - sindicato)
>>>>>>> 41fcc7c66e9c7e7e2f0b092ba21870cdf69d8b8d
print(f"Salario Liquido: R$: {salario_liquido:.2f}")