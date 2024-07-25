print("Informe qual turno estuda: \n M - Matutino \n V - Verspetino \n N - Noturno")
turno = input("Digite:")

if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa tarde!")
elif turno.upper() == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")