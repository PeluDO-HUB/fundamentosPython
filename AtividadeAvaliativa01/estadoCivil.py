estadoC= input("Digite seu estado civil \nC para Casado \nS para solteiro \nD para divorciado \nV para viúvo" 
"\nO para Outros\nEstado Civil: ").upper()


if estadoC=="C":
    print("Você é Casado")
elif estadoC=="S":
    print("Você é Solteiro")
elif estadoC=="D":
    print("Você é Divorciado")
elif estadoC=="V":
    print("você é Viúvo")
elif estadoC =="O":
    print(f"Você esta numa situação complicada amigo, estado civil informado {estadoC}")
else:
    print(f"Dado informado Invalido: {estadoC}")