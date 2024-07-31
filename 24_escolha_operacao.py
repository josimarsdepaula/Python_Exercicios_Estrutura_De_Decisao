def par_ou_impar (resultado):
    return "Par" if (resultado % 2) == 0 else "Ímpar"

def positivo_ou_negativo(resultado):
    if resultado > 0:
        return "Positivo"
    elif resultado < 0:
        return "Negativo"
    else:
        return "Zero ou Nulo"

def inteiro_ou_decimal(resultado):
    return "Inteiro" if resultado == round(resultado) else "Decimal"

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

print("Qual operação deseja fazer?")
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

operacao = float(input("Informe o número da operação: "))
lista_operacao = {
    1: "Soma",
    2: "Subtração",
    3: "Divisão",
    4: "Multiplicação"
}

if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro. Divisão por Zero não é permitida!")
        resultado = None
elif operacao == 4:
    resultado = num1 * num2
else:
    print("Operação inválida.")
    resultado = None

if resultado is not None: 
    print(f"\nO resultado da Operação: {lista_operacao[operacao]} é {resultado:.2f}")
    print(f"Esse valor é: {par_ou_impar(resultado)}")
    print(f"Esse valor é: {positivo_ou_negativo(resultado)}")
    print(f"Esse valor é: {inteiro_ou_decimal(resultado)}")
