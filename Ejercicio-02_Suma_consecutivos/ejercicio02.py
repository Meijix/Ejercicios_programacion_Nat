#Programa que recibe un numero de entrada entre 1 y 50 
#suma los numeros consecutivos hasta llegar a ese numero.

def suma_consecutiva(numero):
    suma = 0
    for i in range(1, numero + 1):
        suma += i  
    return suma

num = int(input("Ingrese un número entre 1 y 50: "))

#Volver a solicitar el numero hasta que el usuario ingrese un numero valido.
while num < 1 or num > 50:
    print("El número ingresado no es válido")
    num = int(input("Ingrese un número entre 1 y 50: "))

print("La suma de sus consecutivos es:", suma_consecutiva(num))
