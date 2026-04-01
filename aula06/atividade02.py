"""
1. Sistema de humor do dia
Crie um programa que pergunte ao usuário como ele está se sentindo hoje (por exemplo: feliz, cansado, estressado, animado). 
Com base na resposta, o programa deve sugerir uma atividade:
Se estiver feliz ou animado, sugerir algo social ou produtivo;
Se estiver cansado, sugerir descanso;
Se estiver estressado, sugerir algo relaxante;
Caso a resposta não esteja prevista, exibir uma mensagem padrão sugerindo uma pausa.
O programa deve responder de forma personalizada para o usuário.
"""

humor=str(input("Olá, Como está se sentindo?\n Responda com feliz, cansado, estressado, animado\n")).lower()

if humor=="feliz" or humor=="f" or humor=="animado" or humor=="a":
    print("Saia com seus amigos")
elif humor=="cansado" or humor=="c":
    print("Fique em casa em descanse!")
elif humor=="estressado" or humor=="e":
    print("Respira e conte ate 10")
else:
    print("emoção não registrada")


"""
2. Validador de senha inteligente
Crie um programa que receba uma senha digitada pelo usuário e avalie seu nível de segurança com base nas seguintes regras:
Se a senha tiver menos de 6 caracteres, é considerada fraca;
Se tiver entre 6 e 8 caracteres, é média;
Se tiver mais de 8 caracteres, é forte;
Caso a senha contenha apenas números, exibir um alerta dizendo que ela é pouco segura, independente do tamanho.
O programa deve informar o nível da senha e possíveis melhorias.
"""

while True:
    senha = input("Digite uma senha: ")
    
    if senha.isdigit():
        print("A senha não pode conter apenas números. Tente novamente.\n")
    else:
        break

if len(senha) < 6:
    print("Nível da senha: Fraca\nInsira mais caracteres")
elif 6 <= len(senha) <= 8:
    print("Nível da senha: Média\nInsira mais caracteres")
else:
    print("Nível da senha: Forte\n Insira mais caracteres")
   
"""
3. Sistema de acesso a um mundo pós-apocalíptico
Crie um programa que simule a entrada de um personagem em um abrigo. 
O usuário deve informar: nível de energia (0 a 100) e se possui um item especial (sim ou não).
Se a energia for menor que 30, o personagem não pode entrar;
Se a energia estiver entre 30 e 70, ele só entra se tiver o item especial;
Se a energia for maior que 70, ele entra automaticamente;
Caso os valores informados sejam inválidos, o programa deve avisar o erro.
O programa deve exibir uma mensagem explicando o resultado da decisão.
"""



print("Você esta entrando num abrigo...")
while True:

    energia=int(input("Quanto de Energia você possui? de 0 a 100: "))
    if energia>=0 and energia<=100:
        item =str(input("Possui item especial? S ou N: ")).lower()
        if item=="s" or item=="sim" or item=="n" or item=="nao"or item=="não":
            break
        else:
            print("Cola as coisa certa ai guri!")
    else:
        print("Cola as coisa certa ai guri!")

if energia < 30:
    print("Você se esforça mas não consegue entrar")
elif energia>=30 and energia<=70:
    if item=="s" or item=="sim":
        print("Você consegue entrar utilizando seu item especial e garantindo um descanso seguro")
    else:
        print("Você se esforça mas não consegue entrar, talvez se estivesse com item especial teria conseguido")
else:
    print("Você entra sem dificuldade e possui um descanso tranquilo")
        