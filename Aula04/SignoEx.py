from datetime import datetime
import os


def menuPrograma():
    print("Escolha qual Exercicio quer ver\nDigite de 1 e 2 os exercicios, 3 limpará o prompt de comando e 4 termina o programa")
    escolha=int(input("Esperando o numero do Exercicio...   "))
    match escolha:
        case 1:
            exercicio01()
        case 2:
            signos()
        case 3:
            os.system("cls")
            menuPrograma()
        case 4:
            print("Finalizando o programa...")
        case _:
            print("Opção invalida tente novamente")
            menuPrograma()



def exercicio01():
    idade=int(input("Digite sua idade: "))
    if(idade<0):
        print("Idade insirida não valida")
        exercicio01()
    elif(idade<=12):
        print("Você é criança")
    elif(idade>=13 and idade<=17):
        print("Você é adolecente")
    elif(idade>=18 and idade<=25):
        print("você é adulto jr")
    elif(idade>=26 and idade<=35):
        print("Você é adulto")
    elif(idade>=36 and idade<=60):
        print("Você é adulto sr")
    else:
        print("Você é idoso")
    menuPrograma()

def signos():
    data_str= input("Digite sua data de nascimento dd/mm/aaaa : ")
    data = datetime.strptime(data_str, "%d/%m/%Y")
    """
    Áries: 21 de março a 20 de abril
    Touro: 21 de abril a 20 de maio
    Gêmeos: 21 de maio a 20 de junho
    Câncer: 21 de junho a 22 de julho
    Leão: 23 de julho a 22 de agosto
    Virgem: 23 de agosto a 22 de setembro
    Libra: 23 de setembro a 22 de outubro
    Escorpião: 23 de outubro a 21 de novembro
    Sagitário: 22 de novembro a 21 de dezembro
    Capricórnio: 22 de dezembro a 20 de janeiro
    Aquário: 21 de janeiro a 18 de fevereiro
    Peixes: 19 de fevereiro a 20 de março
    """
    if (data.month == 1 and data.day >= 21) or (data.month == 2 and data.day <= 18):
        print("Você é de Aquário")
    elif(data.month == 2 and data.day >= 19) or (data.month == 3 and data.day <= 20):
        print("Você é de Peixes")
    elif(data.month == 3 and data.day >= 21) or (data.month == 4 and data.day <= 20):
        print("Você é de áries")
    elif(data.month == 4 and data.day >= 21) or (data.month == 5 and data.day <= 20):
        print("Voce é de Touro")
    elif(data.month == 5 and data.day >= 21) or (data.month == 6 and data.day <= 20):
        print("você é de gemeos")
    elif(data.month == 6 and data.day >= 21) or (data.month == 7 and data.day <= 22):
        print("voce é de cancer")
    elif(data.month == 7 and data.day >= 23) or (data.month == 8 and data.day <= 22):
        print("voce é de leao")
    elif(data.month ==8  and data.day >= 23) or (data.month == 9 and data.day <= 22):
        print("voce é de virgem")
    elif(data.month == 9 and data.day >= 23) or (data.month == 10 and data.day <= 22):
        print("libra")
    elif(data.month == 10 and data.day >= 23) or (data.month == 11 and data.day <= 21):
        print("voce é de escorpiao")
    elif(data.month == 11 and data.day >= 22) or (data.month == 12 and data.day <= 21):
        print("voce é de sargitario")
    else:
        print("voce e de capricornio")
    menuPrograma()

menuPrograma()
