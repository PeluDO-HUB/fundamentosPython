"""
1. Variáveis Simples
Crie
três variáveis e peça elas para o usuário:
Uma chamada cidade que guarde o nome da sua cidade;
Uma chamada ano que guarde o ano atual;
Uma chamada temperatura que guarde um valor numérico representando a
temperatura média da sua cidade;
Em seguida, imprima uma frase completa
usando essas variáveis.
"""

cidade = str(input("Insira o nome de sua Cidade: "))
anoAtual = int(input("Insira o Ano: "))
temp= float(input(f"Insira a temperatura media da Cidade {cidade} no ano de {anoAtual}: "))

print(f"A temperatura media na Cidade de {cidade} no ano {anoAtual} foi de {temp:.1f}°C")

"""
2.
Operações matemáticas
Crie duas variáveis numéricas e peça elas
para o usuário. Realize as seguintes operações matemáticas entre elas:
Soma
Subtração
Multiplicação
Divisão
"""

n1=int(input("Insira o Valor do 1° numero: "))
n2=int(input("Insira o Valor do 2° numero: "))
soma=n1+n2
sub=n1-n2
div=n1/n2
mult=n1*n2

print(f"A Soma: {n1} + {n2} = {soma}\n"+
      f"A Subração: {n1} - {n2} = {sub}\n"+
      f"A Divisão: {n1} / {n2} = {div}\n"+
      f"A Multiplicação: {n1} * {n2} = {mult}")