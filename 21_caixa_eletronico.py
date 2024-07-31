saque = int(input("Digite o valor do saque (entre R$10 e R$600): "))

notas_disponiveis = [100,50,10,5,1]
valor_restante = saque



if saque < 10 or saque > 600:
     print("Valor de saque inválido. O valor deve estar entre R$10 e R$600.")

else:
    # Preparar para armazenar a quantidade de cada nota
    notas_fornecidas = {notas: 0 for notas in notas_disponiveis}

    for notas in notas_disponiveis:
        if valor_restante >= notas:
            quantidade = valor_restante // notas
            notas_fornecidas[notas] = quantidade
            valor_restante -= quantidade * notas
                

  # Mostrar as notas fornecidas
    print("Notas fornecidas:")
    for notas in notas_disponiveis:
        if notas_fornecidas[notas] > 0:
            print(f"{notas_fornecidas[notas]} nota(s) de R${notas}")
        