perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas_sim = 0

for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    
    if resposta != "sim" and resposta != "não":
        print("Erro. Favor responder somente com (sim/não). ")
    else:   
        if resposta == "sim":
            respostas_sim += 1

if respostas_sim == 2:
    print("Suspeita")
elif respostas_sim >= 3 and respostas_sim <= 4:
    print("Cúmplice")
elif respostas_sim == 5:
    print("Assassino")
else:
    print("Inocente")