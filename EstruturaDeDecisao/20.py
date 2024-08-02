<<<<<<< HEAD
# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota_1 = float(input("Digite a primeira nota parcial do aluno: "))
nota_2 = float(input("Digite a segunda nota parcial do aluno: "))
nota_3 = float(input("Digite a terceira nota parcial do aluno: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
        print("Aprovado com a respectiva média alcançada")
elif media < 7:
        print("Reprovado com a respectiva média alcançada")
elif media == 10:
=======
# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota_1 = float(input("Digite a primeira nota parcial do aluno: "))
nota_2 = float(input("Digite a segunda nota parcial do aluno: "))
nota_3 = float(input("Digite a terceira nota parcial do aluno: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
        print("Aprovado com a respectiva média alcançada")
elif media < 7:
        print("Reprovado com a respectiva média alcançada")
elif media == 10:
>>>>>>> 41fcc7c66e9c7e7e2f0b092ba21870cdf69d8b8d
        print("Aprovado com Distinção")