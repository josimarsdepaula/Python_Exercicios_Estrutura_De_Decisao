lado1 = float(input("Informe o valor do primeiro lado do Triângulo: "))
lado2 = float(input("Informe o valor do primeiro lado do Triângulo: "))
lado3 = float(input("Informe o valor do primeiro lado do Triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado3 + lado2 > lado1):
    print("Os valores correspondem a um Triângulo.")

    if lado1 == lado2 == lado3:
        tipo_triangulo = "Triângulo Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Triângulo Isósceles"
    else:
        tipo_triangulo = "Triângulo Escaleno"
    print(f"Esse é um {tipo_triangulo}")
else:
    print("Os valores não correspondem a um Triângulo. Insira os valores novamente!")
