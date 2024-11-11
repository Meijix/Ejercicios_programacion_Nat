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

#Funciones
def obtener_apuesta(dinero):
    while True:
        try:
            apuesta = int(input(f"Ingrese su apuesta entre 20 y 100: "))
            if 20 <= apuesta <= 100 and apuesta <= dinero:
                return apuesta
            else:
                print("Ingrese una apuesta valida: ")
        except ValueError:
            print("Ingrese un numero valido: ")

def obtener_eleccion():
    while True:
        try:
            eleccion = int(input("Elija 1-AGUILA o 0-SOL: "))
            if 0 <= eleccion <= 1:
                return eleccion
            else:
                print("Ingrese una eleccion valida: ")
        except ValueError:
            print("Ingrese un numero valido: ")

def volado_tradicional(volado):
    if volado == 0:
        return "SOL"
    else:
        return "AGUILA"

# Variables iniciales
jugador_dinero = 500
computadora_dinero = 500

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

    # Apuestas
    print("La computadora realiza su apuesta")
    computadora_apuesta = random.randint(20, 100)
    #Se deberia checar que la apuesta de la computadora sea menor a su dinero
    #pero eso no es posible ya que la computadora siempre apuesta entre 20 y 100 y son 3 rondas
    #Si fuera el caso se checa el minimo y se apuesta ese monto o se vuelve a sacar un random con el monto maximo adecuado
    computadora_apuesta = min(computadora_apuesta, computadora_dinero)
    computadora_apuesta = random.randint(20, computadora_apuesta)
    computadora_dinero -= computadora_apuesta
    print(f"La computadora apuesta {computadora_apuesta}")

    jugador_apuesta = obtener_apuesta(jugador_dinero)
    jugador_dinero -= jugador_apuesta

    # Elecciones
    #El jugador siempre elige primero
    #La computadora por default elige el otro valor
    jugador_eleccion = obtener_eleccion()

    if jugador_eleccion == 1:
        print("El jugador eligio AGUILA")
        computadora_eleccion = 0
    else:
        print("El jugador eligio SOL")
        computadora_eleccion = 1

    print(f"La computadora eligio: {computadora_eleccion} que es {volado_tradicional(computadora_eleccion)}")

    # Volado
    print("Volando moneda...")
    time.sleep(3)
    volado = random.randint(0, 1)
    print(f"Resultado del volado: {volado} que es {volado_tradicional(volado)}")
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