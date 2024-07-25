num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o Segundo número: "))
num3 = float(input("Informe o Terceiro número: "))

numeros = [num1, num2, num3]
numeros.sort(reverse= True)

print("Os números em ordem decrescente são:")

for numero in numeros:
    print(numero)