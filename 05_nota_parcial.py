#Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

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