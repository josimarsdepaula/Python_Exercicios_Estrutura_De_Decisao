preco_alcool = 1.90
desc_per_alcool_ate_20 = 0.03
desc_per_alcool_acima_20 = 0.05
preco_gasolina = 2.50
desc_per_gasolina_ate_20 = 0.04
desc_per_gasolina_acima_20 = 0.06

def alcool(litros_alcool):
    if litros_alcool > 0 and litros_alcool <= 20:
        desc_alcool = (litros_alcool * preco_alcool) * desc_per_alcool_ate_20
    elif litros_alcool > 20:
        desc_alcool = (litros_alcool * preco_alcool) * desc_per_alcool_acima_20
    else:
        return None
    return desc_alcool

def gasolina(litros_gasolina):
    if litros_gasolina > 0 and litros_gasolina <= 20:
        desc_gasolina = (litros_gasolina * preco_gasolina) * desc_per_gasolina_ate_20
    elif litros_gasolina > 20:
        desc_gasolina = (litros_gasolina * preco_gasolina) * desc_per_gasolina_acima_20
    else:
        return None
    return desc_gasolina

tipo_combustivel = int(input("Escolha um tipo de combustivel: 1. Alcool, 2. Gasolina:  "))

if tipo_combustivel in (1,2):
    if tipo_combustivel == 1:
        litros_alcool = float(input("Insira a quantidade de Litros de Alcool vendidos: "))
        total_pagar = (litros_alcool * preco_alcool) - alcool(litros_alcool)
        print(f"O valor total a pagar de {litros_alcool:.2f} litros é: R${total_pagar:.2f} reais")
    else:
        litros_gasolina = float(input("Insira a quantidade de Litros de Gasolina vendidos: "))
        total_pagar = (litros_gasolina * preco_gasolina) - gasolina(litros_gasolina)
        print(f"O valor total a pagar de {litros_gasolina:.2f} litros é: R${total_pagar:.2f} reais")
else:
    print("Erro. Insira somente os números (1) para alcool e (2) para Gasolina: ")
