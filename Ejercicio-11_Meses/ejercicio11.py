#Programa que recibe un numero entero entre 0y 11 y muestra el mes correspondiente

#Arreglo con los nombres de los meses ordenados
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

numero = int(input("Ingrese un numero entero entre 0 y 11: "))
if 0 <= numero <= 11:
    print(meses[numero])
else:
    print("El numero ingresado no es valido")

