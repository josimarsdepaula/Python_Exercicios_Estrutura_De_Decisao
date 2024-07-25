#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Informe o Primeiro número: "))
num2 = int(input("Informe o Segundo número: "))
num3 = int(input("Informe o Terceiro número: "))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3


print(f"O Maior número é: {maior}")
print(f"O Menor número é: {menor}")