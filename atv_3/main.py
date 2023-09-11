import json

def MappingAnxiety():
    anxiety = 0
    no_anxiety = 0

    with open("atv_3/questions.json", encoding='utf-8') as json_file:
        questions = json.load(json_file)

    for question in questions:
        answer = input(question["asking"])
        if answer.lower() == "sim":
            if question["id"] == "anxiety":
                anxiety += 1
            else:
                no_anxiety += 1

    return {
        "anxiety": anxiety,
        "no_anxiety": no_anxiety
    }


# Executando a função
users = MappingAnxiety()
# O usuário aprensenta mais respostas com "sim" do que "não"
if users["anxiety"] > users["no_anxiety"]:
    print("DETECTAMOS ANSIEDADE")
    if users["anxiety"] > 8:
        print("Grau III - Encaminhado para Psiquiatria")
    elif users["anxiety"] > 4:
        print("Grau II - Encaminhado para Clínico Geral")
    else:
        print("Grau I - Encaminhado para Enfermaria")
else:
    print("NÃO DETECTAMOS ANSIDEDADE!")
        


