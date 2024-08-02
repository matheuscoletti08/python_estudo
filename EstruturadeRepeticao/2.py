# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

n = 1
while n > 0:
    user = input("Digite seu username: ")
    psswrd = input("Digite sua senha: ")

    if user == psswrd:
        print("Erro! A senha não pode ser igual ao username.")
    else:
        print("Bem-vindo, usuário!")
        break