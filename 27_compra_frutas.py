preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

kg_morango = float(input("Insira a quantidade em (Kg) de morangos adquiridos: "))
kg_maca = float(input("Insira a quantidade em (Kg) de maçãs adquiridas: "))

if 0 <= kg_maca <= 5:
    preco_total_maca = kg_maca * preco_maca_ate_5kg
else:
    preco_total_maca = kg_maca * preco_maca_acima_5kg

if 0 <= kg_morango <= 5:
    preco_total_morango = kg_morango * preco_morango_ate_5kg
else:
    preco_total_morango = kg_morango * preco_morango_acima_5kg


total_quilos_frutas = kg_maca + kg_morango
total_preco_frutas = preco_total_maca + preco_total_morango

if total_quilos_frutas > 8 or total_preco_frutas > 25:
    total_a_pagar = total_preco_frutas * (1 - 0.1)
else:
    total_a_pagar = total_preco_frutas

print("Abaixo a quantidade de frutas e preço a pagar:")
print(f"Morangos: {kg_morango:.2f}Kg")
print(f"Maças: {kg_maca:.2f}Kg")
print(f"Total a pagar: R${total_a_pagar:.2f}")