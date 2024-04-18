# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
sex = input("Digite seu sexo (m/f): ")

if sex == "m":
    height_m = float(input("Digite a sua altura: "))

    peso_ideal_m = (72.8 * height_m) - 58

    print(f"O seu peso ideal é {peso_ideal_m:.2f} kg's")
else:
    height_f = float(input("Digite a sua altura: "))

    peso_ideal_f = (62.1 * height_f) - 58

    print(f"O seu peso ideal é {peso_ideal_f:.2f} kg's")