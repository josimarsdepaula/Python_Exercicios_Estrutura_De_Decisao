import time

valor_hora = float(input("Informa o valor da hora trabalhada: "))
hora_trabalhada = float(input("Informe a quantidade de horas trabalhadas: "))

inicio = time.time()
inss = 0.1
fgts = 0.11
sindicato = 0.035

imposto_per_5 = 0.05
imposto_per_10 = 0.1
imposto_per_20 = 0.2

salario_bruto = valor_hora * hora_trabalhada
desconto_sindicato = salario_bruto * sindicato
desconto_inss = salario_bruto * inss
valor_fgts = salario_bruto * fgts

if salario_bruto <= 900:
    desconto_ir = 0

elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir = salario_bruto * imposto_per_5

elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = salario_bruto * imposto_per_10

else:
    desconto_ir = salario_bruto * imposto_per_20

total_descontos = desconto_ir + desconto_sindicato + desconto_inss
salario_liquido = salario_bruto - total_descontos

print(f"Salario Bruto: R${salario_bruto:.2f}")
print(f" (-) IR (5%) : R${desconto_ir:.2f}")
print(f" (-) INSS (10%) : R${desconto_inss:.2f}")
print(f" (-) Sindicato (3%): R${desconto_sindicato:.2f}")
print(f"FGTS (11%): R${valor_fgts:.2f}\n")
print(f"Total de descontos: R${total_descontos:.2f}")
print(f"Salário Liquido: R${salario_liquido:.2f}")

fim = time.time()
tempo = fim - inicio
print(f"{tempo:.2f}")