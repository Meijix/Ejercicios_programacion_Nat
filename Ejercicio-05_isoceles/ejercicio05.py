#Programa que calcula el perimetro de un triangulo isosceles
#Se pide al usuario que ingrese la longitud de la base y de los lados iguales del triangulo

def calcular_perimetro(base, lado):
    perimetro = base + 2 * lado
    return perimetro

#Debe recibir la longitud de la base y de los lados iguales
print("Perimetro de un triangulo isosceles")
base = float(input("Ingrese la longitud de la base: "))
lado = float(input("Ingrese la longitud de los lados iguales: "))
#Calcula el perimetro del triangulo isosceles
print(f"El perimetro del triangulo isosceles con base de longitud {base} y lados iguales de longitud {lado} es:", calcular_perimetro(base, lado))
