nota1 = float(input("Informe a Primeira Nota parcial: "))
nota2 = float(input("Informe a Segunda Nota parcial: "))

#Calcular a média
media = (nota1 + nota2)/2

if media == 10:
    print("Aprovado com Distinção!")
    
elif media >= 7:
    print("Aprovado!")

else:
    print("Reprovado")