from collections import Counter
import os 

def Calibrate():
    number_cars = int(
        input("Insira a quantidade de carros que deseja no histórico:"))
    vpm = 0
    total_value = 0
    total_weight = 0
    informations_velocity = []
    if number_cars > 0:
        for cars_informations in range(number_cars):
            print("\n \nInsira informações do",
                  cars_informations + 1, "carro:")
            velocity = int(
                input("Insira a velocidade: "))
            accident = int(
                input("Insira se houve acidente com 1 para SIM ou 0 para NÃO:"))
            if velocity > 10 and accident == 0:
                informations_velocity.append(velocity) 
        value_vpm = Counter(informations_velocity)
        vpm_sum = sum(value * count for value, count in value_vpm.items())
        total_values = len(informations_velocity)
        vpm = vpm_sum / total_values
        return vpm


def Velocity_car(vpm):
    velocity= int(input("Qual a velocidade do veículo?"))
    print("velocity =", str(velocity), "vpm =", str(vpm))

    if velocity > vpm:
        print("Veículo Multado!")
    else:
        print("Veículo está OK!") 


print("\n \nDigite 1 para entrar em modo de Calibração, 2 para entrar em modo de execução e  3 para sair")
while 1: 
    print("\n \nRadar em Execução")
    type_opc = int(input("Escolha o modo de operação:"))
    if type_opc == 1:
        vpm = Calibrate()
    elif type_opc == 2:
        if "vpm" in locals():
           Velocity_car(vpm)
        else:
            print("\nNão podmeos iniciar se não houver uma base com dados sobre a Velocidade Máxima Permitada!")
            print("Retorne e faça o abastecimento da base VPM!")
    else: 
        break

        