#Programa en el que el usuario debe adivinar un numero aleatorio entre 1 y 100
#Hint: El programa debe mostrar si el numero ingresado es mayor o menor al numero a adivinar
#El programa debe mostrar cuantos intentos le tomo al usuario adivinar el numero
#El usuario solo tiene 5 intentos para adivinar el numero
#El programa debe mostrar un mensaje de GANASTE si el usuario adivina el numero
#El programa debe mostrar un mensaje de PERDISTE si el usuario no adivina el numero y el numero a adivinar

import random
numero_a_adivinar = random.randint(1, 100)
intentos = 0
print("Adivina el numero entre 1 y 100")
print("Tienes 5 intentos")
print("Buena suerte!")
while intentos < 5:
    intentos += 1
    numero_ingresado = int(input("Ingrese un numero: "))
    if numero_ingresado < numero_a_adivinar:
        print("Intenta un numero mayor")
    elif numero_ingresado > numero_a_adivinar:
        print("Intenta un numero menor")
    else:
        print(f"GANASTE! El numero a adivinar era {numero_a_adivinar}")
        print(f"Se necesitaron {intentos} intentos para adivinar el numero")
        break
else:
    print(f"PERDISTE! El numero a adivinar era {numero_a_adivinar}")
    
