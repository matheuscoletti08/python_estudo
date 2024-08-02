# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
print("Responda com Y ou F")
pergunta1 = str(input("Telefonou para a vítima?: "))
pergunta2 = str(input("Esteve no local do crime?: "))
pergunta3 = str(input("Mora perto da vítima?: "))
pergunta4 = str(input("Devia para a vítima?: "))
pergunta5 = str(input("Já trabalhou com a vítima?: "))
if pergunta1 == Y and pergunta2 == Y and pergunta3 == Y and pergunta4 == Y and pergunta5 ==Y:
    print("Vc é o Assasino")
elif pergunta1 == F and pergunta2 == Y and pergunta3 == Y and pergunta4 == Y and pergunta5 ==Y:
    print("Vc é Cúmplice")       
elif pergunta1 == F and pergunta2 == F and pergunta3 == Y and pergunta4 == Y and pergunta5 ==Y:
    print("Vc é Cúmplice") 
elif pergunta1 == Y and pergunta2 == F and pergunta3 == Y and pergunta4 == Y and pergunta5 ==Y:
    print("Vc é Cúmplice")
elif pergunta1 == Y and pergunta2 == F and pergunta3 == F and pergunta4 == Y and pergunta5 ==Y:
    print("Vc é Cúmplice")  
elif pergunta1 == Y and pergunta2 == Y and pergunta3 == F and pergunta4 == Y and pergunta5 ==Y:
    print("Vc é Cúmplice")  
elif pergunta1 == Y and pergunta2 == Y and pergunta3 == F and pergunta4 == F and pergunta5 ==Y:
    print("Vc é Cúmplice")  
elif pergunta1 == Y and pergunta2 == Y and pergunta3 == Y and pergunta4 == F and pergunta5 ==Y:
    print("Vc é Cúmplice") 