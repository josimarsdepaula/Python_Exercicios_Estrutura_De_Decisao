def ano_bissexto (ano):
    return (ano % 4 == 0 or (ano % 400 == 0 and ano % 100 != 0))

def verifica_data(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False

    if dia < 1:
        return False
    
    if mes == 2:
        if ano_bissexto(ano):
            return dia <= 29
        else:
            return dia <= 28
    elif mes in {4,6,9,11}:
        return dia <= 30
    else:
        return dia <=31

data = input("Digite uma data no formato dd/mm/aaaa: ")

if len(data) != 10 or data[2] != '/' or data[5] != '/':
    print("Data inválida, formato inválido!")

else:
    try:
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])

        if verifica_data(dia, mes, ano):
            print("Data válida!")
        else:
            print("Data Inválida")

    except ValueError:
        print("Data inválida; valores númericos inválidos!")