"""
Um
posto está vendendo combustíveis com a seguinte tabela de descontos: 
Álcool:
->até 20 litros, desconto de 3% no
preço total;
->acima de 20 litros, desconto de 5%
no preço total.
Gasolina:
->até 20 litros, desconto de 4% no
preço total;
->acima de 20 litros, desconto de 6%
no preço total.
Escreva
um algoritmo que leia o número de litros vendidos e o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
pelo cliente sabendo-se que o preço do litro da gasolina é R$ 5,50 e o preço do
litro do álcool é R$ 3,89.
"""
vAlcool=3.89
vGasolina=5.50
while True:
    tipo = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").lower()
    
    if tipo in ["a", "g"]:
        try:
            litros = float(input("Insira a quantidade de litros: "))
            if litros > 0:
                break
            else:
                print("Digite um valor maior que 0!")
        except:
            print("Digite um número válido!")
    else:
        print("Digite apenas A ou G!")

if tipo=="a":
    if litros <=20:
        print(f"Você esta comprando {litros:.1f}L de Alcool que daria o valor de R${(vAlcool*litros):.2f}\n"+
              f"Mas com desconto de 3% o valor será de R$ {((vAlcool*litros)*0.97):.2f}")
    else:
        print(f"Você esta comprando {litros:.1f}L de Alcool que daria o valor de R${(vAlcool*litros):.2f}\n"+
              f"Mas com desconto de 5% o valor será de R$ {((vAlcool*litros)*0.95):.2f}")

if tipo=="g":
    if litros <=20:
        print(f"Você esta comprando {litros:.1f}L de Gasolina que daria o valor de R${(vGasolina*litros):.2f}\n"+
              f"Mas com desconto de 4% o valor será de R$ {((vGasolina*litros)*0.96):.2f}")
    else:
        print(f"Você esta comprando {litros:.1f}L de Gasolina que daria o valor de R${(vGasolina*litros):.2f}\n"+
              f"Mas com desconto de 6% o valor será de R$ {((vGasolina*litros)*0.94):.2f}") 