# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(input("Digite seu salario: "))
if salario <= 280:
    salario_porcentagem = salario*0.2
    salario_total = salario_porcentagem + salario
    print("Salario antes do reajuste: ", salario)
    print("Percentual de aumento aplicado: 20%")
    print("Valor do aumento: ", salario_porcentagem)
    print("Novo salario: ", salario_total)
elif salario > 280 and salario <= 700:
    salario_porcentagem = salario*0.15
    salario_total = salario_porcentagem + salario
    print("Salario antes do reajuste: ", salario)
    print("Percentual de aumento aplicado: 15%")
    print("Valor do aumento: ", salario_porcentagem)
    print("Novo salario: ", salario_total)
elif salario > 700 and salario <= 1500:
    salario_porcentagem = salario*0.1
    salario_total = salario_porcentagem + salario
    print("Salario antes do reajuste: ", salario)
    print("Percentual de aumento aplicado: 10%")
    print("Valor do aumento: ", salario_porcentagem)
    print("Novo salario: ", salario_total)
else:
    salario_porcentagem = salario*0.05
    salario_total = salario_porcentagem + salario
    print("Salario antes do reajuste: ", salario)
    print("Percentual de aumento aplicado: 5%")
    print("Valor do aumento: ", salario_porcentagem)
    print("Novo salario: ", salario_total)