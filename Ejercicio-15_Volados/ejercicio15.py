#Programa que juegue volados con el usuario. El juego tiene 3 rondas
#Al inicio de cada ronda la computadora realiza una apuesta entre 20 y 100.
#Despues el usuario debe ingresar su apuesta entre 20 y 100
#El dinero que apuesten se resta de su total. Amos inician con 500.
#A continuacion el jugador debe elegir AGUILA o SOL
#El programa debe lanzar el volado y mostrar el resultado
#Gana quien adine el resultado del volado.
#El ganador se lleva el dinero de las dos apuestas.
#El programa debe mostrar el resultado de cada ronda y el total de dinero de cada jugador despues de cada ronda.
#Mostrar el numero de ronda actual.
#El programa debe mostrar el resultado final del juego y el total de dinero de cada jugador
#El programa debe mostrar el mensaje de ganador al final del juego.

import random
import time

#Variables iniciales
jugador_dinero = 500
computadora_dinero = 500

#Ronda 1
numero_ronda = 1
rondas_permitidas = 3
print("Bienvenido al juego de volados")
time.sleep(1)
print("El juego tiene 3 rondas")
time.sleep(1)
print("Cada jugador inicia con 500")
time.sleep(1)
print("Que empiece el juego!")
while numero_ronda <= rondas_permitidas:
    print(f"Ronda {numero_ronda}")

    #Apuestas
    print("La computadora realiza su apuesta")
    computadora_apuesta = random.randint(20, 100)
    computadora_dinero -= computadora_apuesta
    print(f"La computadora apuesta {computadora_apuesta}")

    jugador_apuesta = int(input("Ingrese su apuesta entre 20 y 100: "))
    #Validar que la apuesta del jugador sea valida
    if jugador_apuesta < 20 or jugador_apuesta > 100:
        print("Ingrese una apuesta valida: ")
        jugador_apuesta = int(input("Ingrese su apuesta entre 20 y 100: "))
    else:
        pass
    jugador_dinero -= jugador_apuesta
    #Elecciones
    print("Elija 1-AGUILA o 0-SOL")
    jugador_eleccion = int(input("Ingrese su eleccion: "))
    computadora_eleccion = random.randint(0, 1)
    print(f"La computadora eligio: {computadora_eleccion}")
    #Validar que la eleccion del jugador sea valida
    if jugador_eleccion < 0 or jugador_eleccion > 1:
        print("Ingrese una eleccion valida: ")
        jugador_eleccion = int(input("Ingrese su eleccion: "))

    else:
        #Volado
        print("Volando moneda...")
        time.sleep(2)
        volado = random.randint(0, 1)
        if jugador_eleccion == volado:
            print("Ganaste!")
            jugador_dinero += computadora_apuesta + jugador_apuesta
        else:
            print("Perdiste!")
            computadora_dinero += computadora_apuesta + jugador_apuesta

    print(f"Computadora: {computadora_dinero}")
    print(f"Jugador: {jugador_dinero}")

    numero_ronda += 1

print("Fin del juego")
if jugador_dinero > computadora_dinero:
    print("Ganaste!")
elif jugador_dinero < computadora_dinero:
    print("Perdiste!")
else:
    print("Empate!")

print(f"Dinero total CPU: {computadora_dinero}")
print(f"Dinero total Jugador: {jugador_dinero}")
