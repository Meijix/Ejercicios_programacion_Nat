#Programa que calcula el perimetro de un triangulo escaleno
#Se pide al usuario que ingrese la longitud de cada uno de los lados del triangulo

def calcular_perimetro(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

#Debe recibir la longitud de la base y de los lados iguales
print("Perímetro de un triángulo escaleno")
lado1 = float(input("Ingrese la longitud del lado 1: "))
while lado1 <= 0:
    lado1 = float(input("Ingrese una longitud válida para el lado 1: "))

lado2 = float(input("Ingrese la longitud del lado 2: "))
while lado2 <= 0:
    lado2 = float(input("Ingrese una longitud válida para el lado 2: "))

lado3 = float(input("Ingrese la longitud del lado 3: "))
while lado3 <= 0:
    lado3 = float(input("Ingrese una longitud válida para el lado 3: "))

#Calcula el perimetro del triangulo isosceles
print(f"El perímetro del triángulo escaleno con lados {lado1},{lado2}, {lado3} es:", calcular_perimetro(lado1, lado2, lado3))
