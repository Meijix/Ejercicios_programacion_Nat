#Programa que calcula el perimetro de un triangulo equilatero
#Se pide al usuario que ingrese la longitud de un lado del triangulo

#Debe recibir la longitud de uno de sus lados
def calcular_perimetro(lado):
    perimetro = lado * 3
    return perimetro

print("Perímetro de un triángulo equilátero")
#Ingresa la longitud de uno de los lados del triangulo equilatero
longitud_lado = float(input("Ingrese la longitud de uno de los lados: "))
while longitud_lado < 0:
    print("La longitud del lado no puede ser negativa")
    longitud_lado = float(input("Ingrese una longitud válida: "))
print(f"El perímetro del triángulo equilátero con lados de longitud {longitud_lado} es:", calcular_perimetro(longitud_lado))
