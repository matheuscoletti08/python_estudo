<<<<<<< HEAD
# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Qual a medida do primeiro lado do triangulo?: "))
lado2 = float(input("Qual a medida do segundo lado do triangulo?: "))
lado3 = float(input("Qual a medida do terceiro lado do triangulo?: "))

if lado1 == lado2 == lado3:
    print("É um triangulo equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("É um triangulo isosceles")
else:
=======
# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Qual a medida do primeiro lado do triangulo?: "))
lado2 = float(input("Qual a medida do segundo lado do triangulo?: "))
lado3 = float(input("Qual a medida do terceiro lado do triangulo?: "))

if lado1 == lado2 == lado3:
    print("É um triangulo equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("É um triangulo isosceles")
else:
>>>>>>> 41fcc7c66e9c7e7e2f0b092ba21870cdf69d8b8d
    print("É um triangulo escaleno")