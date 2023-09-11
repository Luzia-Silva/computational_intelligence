import json
import os

def MappingAnxiety():
    anxiety = 0
    no_anxiety = 0

    with open("atv_3/assets/json/questions.json", encoding='utf-8') as json_file:
        questions = json.load(json_file)

    for index, question in enumerate(questions):
        answer = input("\n" + str(index + 1) +  " - " + question["asking"]+"\n")
        if answer.lower() == "sim" or answer.lower() == "não":
            if answer.lower() == "sim":
                anxiety += 1
            else:
                no_anxiety += 1
        else: 
            print("Desculpa, mas nosso sistema é capaz somente de entender entradas como (sim/não), retorne e preencha novamente!\n\n")

    return {
        "anxiety": anxiety,
        "no_anxiety": no_anxiety
    }

while True: 
    stopService = input("\n\nDeseja Iniciar o atendimento? (sim/não)\n")

    if stopService.lower() == "sim":
        user = MappingAnxiety()
        if user["anxiety"] > user["no_anxiety"]:
            os.system("clear")
            print("\n\nDETECTAMOS ANSIEDADE")
            if user["anxiety"] >= 8:
                print("Grau II - Encaminhado para Psiquiatria")
            else:
                print("Grau I - Encaminhado para Clínico Geral")
        else:
            os.system("clear")
            print("\n\nNÃO DETECTAMOS ANSIDEDADE!")
    else:
        print("\n\nAgradecemos pela escolha dos nossos serviços! Equipe Anxiety Detection :)")
        exit()



