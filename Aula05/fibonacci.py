anterior = 0
atual = 1

numero=int(input("Digite o limite da Sequencia de Fibonacci: "))    
while anterior <= numero:
        print(anterior)
        proximo = anterior + atual
        anterior = atual
        atual = proximo

       
