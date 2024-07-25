numero1 = int(input("Informe o Primeiro número: "))
numero2 = int(input("Informe o Segundo número: "))
numero3 = int(input("Informe o Terceiro número: "))

if numero1 > numero2 or numero1 > numero3:
    maior = numero1

elif numero2 > numero1 or numero2 > numero3:
    maior = numero2

else:
    maior = numero3

print(f"O Maior número é: {maior}")

