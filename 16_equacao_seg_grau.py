import math

print("Calcule as raízes da equação ax2 + bx + c :")
a = float(input("Informe o valor de (a):"))

if a == 0:
    print("O valor de 'a' não pode ser zero. Essa equação não é do segunda grau!")

else:
    b = float(input("Informe o valor de (b):"))
    c = float(input("Informe o valor de (c):"))

    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("A Equação não possui raizes reais.")

    elif delta == 0:
        raiz = -b / 2*a
        print(f"Valor da raiz é: {raiz:.2f}")

    else:
        raiz1 = (-b+math.sqrt(delta))
        raiz2 = (-b-math.sqrt(delta)/2*a)

        print(f"A Equação possui duas raizes: {raiz1:.2f} e {raiz2:.2f}")

        