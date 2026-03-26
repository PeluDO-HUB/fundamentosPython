
import os


def menuPrograma():
    print("Escolha qual Exercicio quer ver\nDigite 1 para adicionar as notas do aluno,2 para adicionar a quantidade de turmas e alunos,\n" \
    "3 contador de casas do numero inserido,4 criador de senhas e 5 calculadora, 6 eventos, 7 limpará o prompt de comando e 8 termina o programa")
    escolha=int(input("Esperando o numero do Exercicio...   "))
    match escolha:
        case 1:
            mediaAluno()
        case 2:
            mediaTurma()
        case 3:
            contadorCasa()
        case 4:
            criadorSenhas()
        case 5:
            calculadora()
        case 6:
            evento()
        case 7:
            os.system("cls")
            menuPrograma()
        case 8:
           print("Finalizando o programa...")
        case _:
            print("opção invalida")
            menuPrograma()
           
def mediaAluno():
    qtdnotas=int(input("Insira a quantidade de notas a serem inseridas "))
    contagem = 0
    somaNota = 0


    while qtdnotas>0:
        
        nota = float(input(f"Insira a {contagem+1}° nota: "))
        if nota<=10 and nota>=0:        
            qtdnotas-=1
            somaNota +=nota
            print(f"Nota de {nota:.2f} inserida")
            contagem+=1
        else:
            print("Nota invalida")       
    else:
        media = somaNota/contagem
        print(f"A media do aluno foi de {media:.2f}")
    print("")
    menuPrograma()

    
def mediaTurma():
    qtdTurma = int(input("Digite a quantidade de turmas: "))
    contagem = 0
    if qtdTurma <=0:
        print("Quantidade de turmas invalida")
        mediaTurma()
    somaAluno = 0
    while qtdTurma > 0:
        qtdAluno =int(input(f"Insira a quantidade de Alunos na {contagem+1}° turma: "))
        if qtdAluno <=40 and qtdAluno > 0:
            qtdTurma-=1
            somaAluno+=qtdAluno
            contagem+=1
            print(f"Turma {contagem} possui {qtdAluno} alunos")
        else:
            print("Quantidade de Alunos invalida, Cada turma só pode possuir no maximo 40 alunos e no minimo 1")
    else:
        mediaAluno = somaAluno/contagem
        print(f"A media de alunos por sala é de {mediaAluno:.0f}")
    print("")
    menuPrograma()

def contadorCasa():
    num=int(input("Insira um numero inteiro para contagem de casas:"))
    contagem = 0
    if num < 0:
        num = -num
    elif num==0:
        contagem=1
    else:
        while num > 0:
            num = num // 10
            contagem+=1
        else:
            print(f"Quantidade de casas é de {contagem}")
            print("")
            menuPrograma()



def criadorSenhas():
    senha=str(input("Crie uma senha: "))

    verificador=str(input("Digite a senha novamente: "))

    while senha!=verificador :
        verificador=str(input("Senhas diferentes, digite a senha novamente: "))
    else:
        print("Senha gravada com sucesso")
        print("")
        menuPrograma()


def calculadora():
    

    numeroIns=int(input("Digite um Valor a ser somado, ao digitar 0 finaliza a soma e mostra o resultado: "))
    contador = 0
    SomaIns = 0

    while numeroIns != 0:
        if numeroIns <=0:
            print("numero invalido")
            numeroIns=int(input("Digite um Valor a ser somado: "))
        else:
            contador+=1
            SomaIns+= numeroIns
            numeroIns=int(input("Digite um Valor a ser somado: "))
    
    if contador == 0 or contador==1:
        print("Pra que a calculadora amigo?")
    else:
        print(f"A soma de todos os {contador} numeros é de {SomaIns}")
    print("")
    menuPrograma()


def evento():

    qtdPessoas=int(input("Digite a quantidade de pessoas "))
    contador=0
    qtdEntrou=0
    while qtdPessoas > contador:
        
        contador+=1

        idade=int(input(f"Digite a idade da {contador}° pessoa: "))
        if idade <16:
            print("Menores de 16 anos não entram")
        elif idade>=16 and idade<18:
            permissao=int(input("Possui convite? Digite 1 para sim e 0 para não: "))
            if permissao==1:
                print("Entrada Liberada")
                qtdEntrou+=1
            else:
                print("Permissão de pessoas de 16 e 17 anos apenas com convite, Acesso negado!")
        else:
            qtdEntrou+=1
            print("Aproveite a festa")
    print(f"A quantidade de pessoas que tentaram entrar foi de {qtdPessoas} e {qtdEntrou} conseguiram entrar")
    print("")
    menuPrograma()
    
menuPrograma()