#Programa que calcula el perimetro de un triangulo isosceles
#Se pide al usuario que ingrese la longitud de la base y de los lados iguales del triangulo

def calcular_perimetro(base, lado):
    perimetro = base + (2 * lado)
    return perimetro

#Debe recibir la longitud de la base y de los lados iguales
print("Perimetro de un triangulo isosceles")
base = float(input("Ingrese la longitud de la base: "))
while base < 0:
    print("La longitud de la base no puede ser negativa")
    base = float(input("Ingrese una longitud válida: "))

lado = float(input("Ingrese la longitud de los lados iguales: "))
while lado < 0:
    print("La longitud de los lados iguales no puede ser negativa")
    lado = float(input("Ingrese una longitud válida: "))
#Calcula el perimetro del triangulo isosceles
print(f"El perímetro del triángulo isóceles con base de longitud {base} y lados iguales de longitud {lado} es:", calcular_perimetro(base, lado))
