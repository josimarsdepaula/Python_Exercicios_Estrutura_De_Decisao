#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Informe uma letra: ")

if letra.upper() in ("A", "E", "I", "O", "U"):
    print("Essa letra é uma Vogal.")
    
else:
    print("Essa letra é uma consoante.")