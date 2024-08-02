# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota_parc1 = float(input("Digite a primeira nota do aluno: "))
nota_parc2 = float(input("Digite a segunda nota do aluno: "))

media_notas = (nota_parc1 + nota_parc2) / 2

if media_notas >= 9.0:
        print(f"A media foi {media_notas} e a mençao é A")

elif media_notas >= 7.5:
        print(f"A media foi {media_notas} e a mençao é B")

elif media_notas >= 6.0:
        print(f"A media foi {media_notas} e a mençao é C")

elif media_notas >= 4.0:
        print(f"A media foi {media_notas} e a mençao é D")

else:
        print(f"A media foi {media_notas} e a mençao é E")