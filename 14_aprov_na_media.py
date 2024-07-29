nota1 = float(input("Informe a primeira nota da matéria: "))
nota2 = float(input("Informe a segunda nota da matéria: "))

media = (nota1 + nota2)/2

if 9.0 < media <= 10.0:
    conceito = "A"
elif 7.5 < media <= 9.0:
    conceito = "B"
elif 6.0 < media <= 7.5:
    conceito = "C"
elif 4.0 < media <= 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A","B","C"]:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print(f"Primeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Média notas: {media}")
print(f"O Aluno está {situacao}")