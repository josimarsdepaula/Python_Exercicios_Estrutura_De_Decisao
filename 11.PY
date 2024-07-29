'''Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
1. o salário antes do reajuste;
2. o percentual de aumento aplicado;
3. o valor do aumento;
4. o novo salário, após o aumento.*/'''

salario = float(input("Informe o Seu salário:"))

aumento_per_20 = 0.2
aumento_per_15 = 0.15
aumento_per_10 = 0.1
aumento_per_05 = 0.05

if salario <= 280:
    valor_aumento = salario * aumento_per_20
    novo_salario = valor_aumento + salario
    percentual = "20%"

elif salario > 280 and salario <= 700:
    valor_aumento = salario * aumento_per_15
    novo_salario = salario + valor_aumento
    percentual = "15%"

elif salario > 700 and salario <= 1500:
    valor_aumento = salario * aumento_per_10
    novo_salario = salario + valor_aumento
    percentual = "10%"
else:
    valor_aumento = salario * aumento_per_05
    novo_salario = salario + valor_aumento
    percentual = "05%"

print(f"Seu salario antes do Ajuste: R${salario:.2f}") 
print(f"O percentual de aumento aplicado foi: {percentual}")
print(f"O valor do aumento: R${valor_aumento:.2f}")
print(f"Seu novo salário após o aumento é: R${novo_salario:.2f}")
