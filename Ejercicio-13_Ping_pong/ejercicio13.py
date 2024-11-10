#Ejercicio Ping Pong
#Programa que imprime los numeros del 1 al 100. Pero para los multiplos de 3 imprime "ping" en lugar del numero y para los multiplos de 5 imprime "pong". Para los numeros que son multiplos de 3 y 5 imprime "ping pong".

def ping_pong():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("ping pong")
        elif i % 3 == 0:
            print("ping")
        elif i % 5 == 0:
            print("pong")
        else:
            print(i)

ping_pong()