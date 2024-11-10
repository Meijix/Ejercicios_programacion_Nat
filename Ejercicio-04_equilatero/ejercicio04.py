#Programa que calcula el perimetro de un triangulo equilatero
#Se pide al usuario que ingrese la longitud de un lado del triangulo

#Debe recibir la longitud de uno de sus lados
def calcular_perimetro(lado):
    perimetro = lado * 3
    return perimetro

#Ejemplo de uso
#Ingresa la longitud de uno de los lados del triangulo equilatero
long_lado = float(input("Ingrese la longitud de uno de los lados del triangulo equilatero: "))
print(f"El perimetro del triangulo equilatero con lados de longitud {long_lado} es:", calcular_perimetro(long_lado))
