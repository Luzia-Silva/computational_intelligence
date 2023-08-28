def Calibrate():
    number_cars = int(
        input("Insira a quantidade de carros que deseja no histórico:"))
    vpm = 0
    informations_velocity = []
    if number_cars > 0:
        for cars_informations in range(number_cars):
            calculo = int(cars_informations + 1) * 2
            print(calculo)
            print("\n \nInsira informações do",
                  cars_informations + 1, "carro:")
            velocity = int(
                input("Insira a velocidade: "))
            accident = int(
                input("Insira se houve acidente com 1 para SIM ou 0 para NÃO:"))
            if velocity > 10 and accident in [0, 1]:
                informations_velocity.append([velocity, accident])

        print("Velocidade Máxima Permitida: " + str(vpm))
    if informations_velocity:
        print(informations_velocity[0][0])


Calibrate()
