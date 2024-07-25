#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.


prod1 = float(input("Informe o valor do Primeiro produto: "))
prod2 = float(input("Informe o valor do Segundo produto: "))
prod3 = float(input("Informe o valor do Terceiro produto: "))

if prod1 < prod2 or prod1 < prod3:
    menor = prod1
    print(f"O Produto com menor valor é o Primeiro Produto. R${menor}")
elif prod2 < prod1 or prod2 < prod3:
    menor = prod2
    print(f"O Produto com menor valor é o Segundo Produto. R${menor}")
else:
    menor = prod3
    print(f"O Produto com menor valor é o Terceiro Produto. R${menor}")
