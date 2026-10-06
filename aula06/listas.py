


class idade:
    def __init__(self, valor=0):
        self.valor = self.validar_idade(valor)

    def validar_idade(self, valor):
        try:
            valor = int(valor)
        except (TypeError, ValueError):
            raise ValueError("A idade deve ser um número inteiro.")

        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")

        return valor

    def categoria(self):
        if self.valor < 13:
            return "criança"
        if self.valor < 18:
            return "adolescente"
        if self.valor < 60:
            return "adulto"
        return "idoso"

    def adicionar_anos(self, anos):
        anos = self.validar_idade(anos)
        self.valor += anos
        return self.valor

    def __str__(self):
        return f"{self.valor} anos ({self.categoria()})"


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
qtdalunos = int(input("Digite a quantidade de alunos a serem inseridos: "))
for i in range(qtdalunos):
    nome = input("Digite o nome: ")
    
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0 or idade > 18:
                print("Idade inválida, digite novamente")
            else:
                break
        except ValueError:
            print("Digite apenas números inteiros para a idade.")
    
    
    while True:
        try:
            altura = float(input("Digite a altura: "))

            if altura <= 0 or altura > 3:
                print("Altura inválida, digite novamente")
            else:
                break
        except ValueError:
            print("Digite Um número válido para a altura.")
    
    alunos.append([nome, idade, altura])
    print(alunos[i])
    totalAltura += altura

mediaAltura = totalAltura / qtdalunos
alunos13 = 0

for i in range(len(alunos)):
    if alunos[i][1] > 13 and alunos[i][2] >= mediaAltura:
        alunos13 += 1

print("Média de altura dos alunos:", mediaAltura)
print("Quantidade de alunos com idade maior que 13 que estão na media ou acima da media:", alunos13)

