<<<<<<< HEAD
# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

if mes >= 1 and mes <= 12 and dia <= 31:
        print("Data valida")
else:
=======
# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

if mes >= 1 and mes <= 12 and dia <= 31:
        print("Data valida")
else:
>>>>>>> 41fcc7c66e9c7e7e2f0b092ba21870cdf69d8b8d
        print("Data invalida")  