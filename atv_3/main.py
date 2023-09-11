import json

def MappingAnxiety():
    anxiety = 0
    no_anxiety = 0

    with open("atv_3/assets/json/questions.json", encoding='utf-8') as json_file:
        questions = json.load(json_file)

    for question in questions:
        answer = input(question["asking"])
        if answer.lower() == "sim":
            anxiety += 1
        else:
            no_anxiety += 1

    return {
        "anxiety": anxiety,
        "no_anxiety": no_anxiety
    }

# Executando a função
user = MappingAnxiety()

# O usuário aprensenta mais respostas com "sim" do que "não"
if user["anxiety"] > user["no_anxiety"]:
    print("DETECTAMOS ANSIEDADE")
    if user["anxiety"] > 8:
        print("Grau III - Encaminhado para Psiquiatria")
    elif user["anxiety"] > 4:
        print("Grau II - Encaminhado para Clínico Geral")
    else:
        print("Grau I - Encaminhado para Enfermaria")
else:
    print("NÃO DETECTAMOS ANSIDEDADE!")
        


