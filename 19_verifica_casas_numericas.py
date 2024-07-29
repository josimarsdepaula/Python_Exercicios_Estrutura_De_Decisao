num = int(input("Informe um número menor que 1000: "))

if int(num) >= 1000 or int(num) < 0:
    print("Número inválido! Insira um número menor que 1000.")

else:
    centena = num // 100
    dezena = (num % 100) // 10
    unidade = num % 10

    resultado = []

    #Verifica Centena
    if centena > 0:
        if centena == 1:
            resultado.append("1 centena")
        else:
            resultado.append(f"{centena} centenas")

    #Verifica Dezena
    if dezena > 0:
        if dezena == 1:
            resultado.append("1 dezena")
        else:
            resultado.append(f"{dezena} dezenas")

    #Verifica Unidade
    if unidade > 0:
        if unidade == 1:
            resultado.append("1 unidade")
        else:
            resultado.append(f"{unidade} unidades")
    
    if len(resultado) == 1:
        print(resultado[0])

    elif len(resultado) == 2:
        print(f"{resultado[0]} e {resultado[1]}")
    
    elif len(resultado) == 3:
        print(f"{resultado[0]}, {resultado[1]} e {resultado[2]}")
    
    else:
        print("0 unidades.")


    

        




