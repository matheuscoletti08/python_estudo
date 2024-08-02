# Faça um programa que leia e valide as seguintes informações:

#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';
 
n = 1
while n == 1:
    name = input("digite seu nome: ")
    if len(name) > 3:
        print("nome válido")
        break
    else:
        print("nome inválido")
        continue

while n == 1:
    age = int(input("digite sua idade: "))
    if age > 0 and age <= 150:
        print("idade valida")
        break
    else:
        print("idade invalida")
        continue

while n == 1:
    salarie = int(input("Digite o seu salario: "))
    if salarie < 0:
        print("salario invalido")
        continue
    else:
        print("salario válido")
        break

while n == 1:
    sex = input("digite seu sexo (m or f): ")
    if sex == "f":
        print("Sexo Feminino")
        break
    elif sex == "m":
        print("Sexo Masculino")
        break
    else:
        print("Sexo Invalido")
        continue

while n == 1:
    civil = input("digite seu estado civil (s, c, v, d): ")
    if civil == "s":
        print("solteiro")
        break
    elif civil == "c":
        print("casado")
        break
    elif civil == "v":
        print("viuvo")
        break
    elif civil == "d":
        print("divorciado")
        break
    else: 
        print("estado civil invalido")
        continue

