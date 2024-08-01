preco_file_ate_5kg = 4.90
preco_file_acima_5kg = 5.80
preco_alcatra_ate_5kg = 5.90
preco_alcatra_acima_5kg = 6.80
preco_picanha_ate_5kg = 6.90
preco_picanha_acima_5kg = 7.80

lista_tipo_carnes = [
    "1 - Filé Duplo",
    "2 - Alcatra",
    "3 - Picanha"
]

lista_tipo_pagamento = [
    "1 - Dinheiro",
    "2 - Cartão Tabajara"
]

#Função para Calcular
def calcula_preco(tipo_carne, total_quilos, tipo_pagamento):
    if tipo_carne == 1:
        if 0 < total_quilos <= 5:
            total_a_pagar = total_quilos * preco_file_ate_5kg
        else:
            total_a_pagar = total_quilos * preco_file_acima_5kg
    elif tipo_carne == 2:
        if 0 < total_quilos <= 5:
            total_a_pagar = total_quilos * preco_alcatra_ate_5kg
        else:
            total_a_pagar = total_quilos * preco_alcatra_acima_5kg
    else:
        if 0 < total_quilos <= 5:
            total_a_pagar = total_quilos * preco_picanha_ate_5kg
            
        else:
            total_a_pagar = total_quilos * preco_picanha_acima_5kg
            
    if tipo_pagamento == 1:
        total_com_desconto = total_a_pagar
        valor_desconto = 0
    else:
        total_com_desconto = total_a_pagar * (1 - 0.05) 
        valor_desconto = total_a_pagar * 0.05

    return total_com_desconto, total_a_pagar, valor_desconto

#Entrada de Dados - Escolha de Tipo de Carne e Quantidade:
print("Escolha um tipo de carne:")
for carne in lista_tipo_carnes:
    print(carne)
tipo_carne = int(input("Informe qual o tipo de carne. Digite um número:"))


while tipo_carne not in (1,2,3):
    print("Opção Inválida! Por favor digite um número novamente.")

    for carne in lista_tipo_carnes:
        print(carne)
    
    tipo_carne = int(input("Informe qual o tipo de carne. Digite um número:"))
total_quilos = float(input("Informe a quantidade de carnes em Kg: "))
    

#Entrada de Dados - Escolha de Tipo de Pagamento:
for pagamento in lista_tipo_pagamento:
    print(pagamento)

tipo_pagamento = int(input("Informe o método de pagamento:"))

while tipo_pagamento not in (1,2):
    print("Opção Inválida! Por favor digite um número novamente.")
    for pagamento in lista_tipo_pagamento:
        print(pagamento)
    tipo_pagamento = int(input("Informe o método de pagamento:"))

a,b,c = calcula_preco(tipo_carne, total_quilos, tipo_pagamento)

print("##### CUPOM FISCAL #####")
print(f"Tipo de Carne:{lista_tipo_carnes[tipo_carne - 1].split(" - ")[-1]}---- {total_quilos:.2f}Kg")
print(f"Preço Total; R${b:.2f}")
print(f"Tipo de Pagamento: {lista_tipo_pagamento[tipo_pagamento -1].split(" - ")[-1]}")
print(f"Valor do Desconto R${c:.2f}")
print(f"Total a Pagar: R${a:.2f}")