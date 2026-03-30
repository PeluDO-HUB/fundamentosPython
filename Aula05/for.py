
import os
def menuPrograma():
    print("Escolha qual Exercicio quer ver\nDigite 1 a 5 para os exercicios, 6 limpará o prompt de comando e 7 termina o programa")
    escolha=int(input("Esperando o numero do Exercicio...   "))
    match escolha:
        case 1:
            sexo()
        case 2:
            numPar()
        case 3:
            media()
        case 4:
            senha()
        case 5:
            fibonachi()
        case 6:
            os.system("cls")
            menuPrograma()
        case 7:
           print("Finalizando o programa...")
        case _:
            print("opção invalida")
            menuPrograma()

"""
1. Desenvolva
um programa que funcione da seguinte maneira: Solicite ao usuário que informe a
quantidade total de pessoas em um grupo. Para cada pessoa, peça que o
usuário registre o sexo, utilizando a letra 'm' ou 'M' para masculino. O programa deve contar e, ao final,
exibir o total de pessoas do sexo masculino.
"""
def sexo():
    qtdPessoas= int(input("Digite a quantidade de pessoas: "))
    masc = 0
    fem = 0
    for pessoa in range(0,qtdPessoas,1):
        genero = input(f"Insira o genero da {pessoa+1}° pessoa\nM para Masculino e F para feminino ").upper()
        if genero == "M" or genero=="MASCULINO":
            masc+=1
            print("Homem registrado!")
        elif genero =="F" or genero=="FEMININO":
            fem+=1
            print("Mulher registrada")
    else:
        print(f"Foram adicionadas {qtdPessoas}, {masc} eram Homens e {fem} eram Mulheres")

    menuPrograma()



"""
2. Desenvolva
um programa em Python que utilize os comandos aprendidos para identificar e
exibir todos os números pares entre 1 e 100.
"""

def numPar():
    for i in range(0,100,1):
        if i%2==0:
            print(i)
        else:
            continue
    menuPrograma()

"""
3. Crie
um programa que leia 5 números e calcule a soma e a média desses números,
exibindo os resultados.
"""
def media():
    soma = 0
    for i in range(1,5,1):
        soma+= int(input(f"Digite o {i}° Numero a ser adicionado: "))
        print(soma)
    else:
        print(f"{soma} / 5 = {soma/i}")
    menuPrograma()



"""
4. Desenvolva um programa que solicite ao usuário um nome e uma senha,
garantindo que a senha não seja igual ao nome de usuário. Se forem iguais,
exiba uma mensagem de erro e peça as informações novamente.
"""
def senha():
    for i in range(0,5,1):
        nome = input("Digite seu nome de Usuario:")
        senha = input("Digite sua senha: ")
        if senha == nome:
            print("Nome de Usuario e senha Iguais, tente novamente!")
            continue
        else:
            print("Cadastro Concluido!")
            break
    else:
        print("Cadastro não concluido!")
    menuPrograma()


def fibonachi():
    anterior = 0
    atual = 1
    qtd=int(input("Quantidade de numeros de Fibonacci a serem exibidos: "))
    for i in range(qtd):
        print(anterior)
        proximo = anterior + atual
        anterior = atual
        atual = proximo
    

menuPrograma()