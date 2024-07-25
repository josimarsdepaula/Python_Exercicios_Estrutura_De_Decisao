#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Informe uma letra: ")

if letra.upper() == "F":
    print(f"A letra digitada é: F - Feminino")

elif letra.upper() == "M":
    print("A Letra digitada é: M - Masculino")

else:
    print(f"Sexo Inválido!")

