n1 = int(input("Insira um numero: "))
n2 = int(input("Insira o segundo numero: "))

if n1==n2:
    print(f"os numeros são iguais")
elif n1<n2:
    print(f"o primeiro numero: {n1} é menor que o segundo numero: {n2}")
else:
    print(f"o segundo numero: {n2} é menor que o primeiro numero: {n1}")
