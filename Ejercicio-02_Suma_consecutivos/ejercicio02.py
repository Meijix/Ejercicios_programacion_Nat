#Programa que recibe un numero de entrada entre 1 y 50 
#suma los numeros consecutivos hasta llegar a ese numero.
#Ejemplo:
#Si el usuario ingresa 10, el programa debe mostrar 1+2+3+4+5+6+7+8+9+10 = 55

def suma_consecutiva(numero):
    suma = 0
    for i in range(1, numero + 1):
        suma += i  
    return suma

#print(suma_consecutiva(10))  # Output: 55

num = int(input("Ingrese un numero entre 1 y 50: "))

if 1 <= num <= 50:
    print("La suma de sus consecutivos es:", suma_consecutiva(num))
else:
    print("El numero ingresado no es valido")  #Si el usuario ingresa un numero fuera del rango, el programa debe mostrar un mensaje de error.