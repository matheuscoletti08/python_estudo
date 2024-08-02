<<<<<<< HEAD
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Digite o numero do produto 1: "))
prod2 = float(input("Digite o numero do produto 2: "))
prod3 = float(input("Digite o numero do produto 3: "))

if prod1 < prod2 and prod1 < prod3:
    print(f"O produto 1 é o mais barato e custa {prod1}")
elif prod2 < prod1 and prod2 < prod3:
    print(f"O produto 2 é o mais barato e custa {prod2}")
else:
=======
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Digite o numero do produto 1: "))
prod2 = float(input("Digite o numero do produto 2: "))
prod3 = float(input("Digite o numero do produto 3: "))

if prod1 < prod2 and prod1 < prod3:
    print(f"O produto 1 é o mais barato e custa {prod1}")
elif prod2 < prod1 and prod2 < prod3:
    print(f"O produto 2 é o mais barato e custa {prod2}")
else:
>>>>>>> 41fcc7c66e9c7e7e2f0b092ba21870cdf69d8b8d
    print(f"0 produto 3 é o mais barato e custa {prod3}")