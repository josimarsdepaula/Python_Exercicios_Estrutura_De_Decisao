nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))
nota3 = float(input("informe a terceira nota: "))

if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <=  nota3 <= 10):
    print("informe uma nota válida")

else:
    media = (nota1 + nota2 + nota3) / 3

    if media == 10:
        print("Aprovado com Distinção")

    elif media >= 7:
        print("Aprovado")
    
    else:
        print("Reprovado")
        
    

