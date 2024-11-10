#Programa que recibe un numero e imprime la tabla de multiplicar de ese numero del 2 al 10
def tabla_multiplicar(numero):
    for i in range(2, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

