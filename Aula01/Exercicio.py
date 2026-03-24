nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4


if media>= 7:
    print(f"Aluno aprovado com a media de {media:.1f}")
elif media >=5:
    print(f"Aluno em Recuperação com a media de {media:.1f}")
else: 
    print(f"Aluno reprovado com a media de {media:.1f}")




