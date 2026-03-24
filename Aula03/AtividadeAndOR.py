import os

def menuPrograma():
    print("Escolha qual Exercicio quer ver\nDigite de 1 a 4 os exercicios, 5 limpará o prompt de comando e 6 termina o programa")
    escolha=int(input("Esperando o numero do Exercicio...   "))
    match escolha:
        case 1:
            exercicio01()
        case 2:
            exercicio02()
        case 3:
            exercicio03()
        case 4:
            exercicio04()
        case 5:
            os.system("cls")
            menuPrograma()
        case 6:
            print("Finalizando o programa...")
        case _:
            print("Opção invalida tente novamente")
            menuPrograma()
            
    



def exercicio01():
    os.system("cls")
    print("Exercicio 01\n"
        "Crie um programa em Python que peça a idade de uma pessoa e se ela possui autorização dos responsáveis (responda com sim ou não).\n"
        "O programa deve permitir a entrada no evento caso a pessoa tenha 18 anos ou mais ou tenha autorização.\n" 
        "Caso contrário, deve informar que a entrada não é permitida.")
    idade = int(input("Digite sua idade: "))
    permition = input("Você possui a permissão para entrar? Responda com sim ou não: ").upper()
    if idade >=18 or permition=="SIM" or permition=="S":
        print("Seja bem vindo ao evento!")
    else:
        print("Você não pode entrar, procure permissão ou espere fazer 18 anos!")
    print("Retornando para menu")
    menuPrograma()

def exercicio02():
    os.system("cls")
    print("Exercicio 02\n"
          "Crie um programa que receba a nota final de um aluno e sua frequência (em porcentagem).\n"
          "O aluno será considerado aprovado se tiver nota maior ou igual a 7 ou frequência maior ou igual a 75%.\n"
          "Caso contrário, deverá ser reprovado. O programa deve exibir uma mensagem informando a situação do aluno.")
    nota=float(input("Digite a nota do aluno: "))
    frequencia=int(input("Digite a frequencia do aluno: "))
    if nota>=7 or frequencia>=75:
        print(f"Aluno aprovado com nota {nota} e frequencia de {frequencia}%")
    else:
        print(f"Aluno reprovado com nota {nota} e frequencia de {frequencia}%")
    print("Retornando para menu")
    menuPrograma()

def exercicio03():
    os.system("cls")
    print("Exercicio 03\n" 
        "Crie um programa que peça o nome de usuário e a senha.\n"
        "O sistema deve permitir o acesso apenas se o usuário for admin e a senha for 1234.\n" 
        "Caso contrário, deve exibir uma mensagem de acesso negado.")
    user=input("Digite seu Usuario: ").lower()
    senha=input("Digite sua Senha: ")
    if user=="admin" and senha=="1234":
        print(f"Acesso liberado!\nBem vindo {user}")
    else:
        print("Acesso negado")
    print("Retornando para menu")
    menuPrograma()

def exercicio04():
    os.system("cls")
    print("Exercicio 04\n"
          "Crie um programa que receba o salário de um funcionário e seu tempo de empresa (em anos).\n" 
          "O funcionário receberá um bônus apenas se tiver salário menor que 3000 e tempo de empresa maior ou igual a 2 anos.\n" 
          "Caso contrário, não receberá bônus. O programa deve exibir uma mensagem informando se o bônus foi concedido ou não.")
    salario=float(input("Digite seu salario: "))
    tempoEmpresa=int(input("Digite seu tempo de empresa em anos: "))
    if salario>=3000 and tempoEmpresa >=2:
        print("Parabens, você receberá o Bonus")
    else:
        print("Que pena você não receberá o bonus ;_;")
    print("Retornando para menu")
    menuPrograma()

menuPrograma()