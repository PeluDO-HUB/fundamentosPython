
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