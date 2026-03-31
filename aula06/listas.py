


def lista():
    num = [1,2,3,4,5]

    print(num)




    num2 =[1,3,2,40,23,10,6,21,0,99]
    num2.reverse()
    print(num2)




    notas = []
    qtd = int(input("Insira a quantidade de notas a serem inseridas na lista: "))
    total = 0
    for i in range(0,qtd,1):
        var = float(input(f"insira o {i+1}° nota: "))
        notas.append(var)
        total+=var
    else:
        print(f"As notas {notas} tem media de {total/qtd:.2f}")
        


alunos=[]
totalAltura=0
for i in range(30):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    
    alunos.append([nome, idade, altura])
    print(alunos[i])
    totalAltura += altura

mediaAltura = totalAltura / 30
alunos13 = 0

for i in range(len(alunos)):
    if alunos[i][1] > 13 and alunos[i][2] >= mediaAltura:
        alunos13 += 1

print("Média de altura dos alunos:", mediaAltura)
print("Quantidade de alunos com idade maior que 13 que estão na media ou acima da media:", alunos13)

