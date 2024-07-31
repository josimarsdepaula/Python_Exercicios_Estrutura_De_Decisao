num = float(input("Informe um número inteiro ou decimal: "))

valor_arredondado = round(num)

if num == valor_arredondado:
    print(f"O número {num:.2f} é inteiro")
else:
    print(f"O número {num:.2f} é decimal")