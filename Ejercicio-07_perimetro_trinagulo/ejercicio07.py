#Programa que calcula el perimetro de un triangulo
#Toma en cuenta el tipo de triangulo que es
# Se pide al usuario que ingrese las entradas necesarias, dependiendo del tipo de triangulo

#Funcion que dependiendodel numero de parametros va a calcular el perimetro de un triangulo
#Recibe los parametros necesarios para calcular el perimetro de un triangulo
def calcular_perimetro(opcion):

    if opcion == 1:
        long_lado = float(input("Ingrese la longitud de uno de los lados del triangulo equilatero: "))
        perimetro = long_lado * 3
    elif opcion == 2:
        base = float(input("Ingrese la longitud de la base: "))
        lado = float(input("Ingrese la longitud de los lados iguales: "))
        perimetro = base + 2 * lado
    elif opcion == 3:
        lado1 = float(input("Ingrese la longitud del lado 1: "))
        lado2 = float(input("Ingrese la longitud del lado 2: "))
        lado3 = float(input("Ingrese la longitud del lado 3: "))
        perimetro = lado1 + lado2 + lado3
    else:
        print("Opcion invalida")
    return perimetro

#preguntar tipo de triangulo usando una funcion
def tipo_triangulo():
    print("Ingresa el numero correspondiente a tu tipo de triangulo")
    print("1. Triangulo equilatero")
    print("2. Triangulo isosceles")
    print("3. Triangulo escaleno")
    opcion = int(input("Ingrese el tipo de triangulo: "))
    return opcion


#Llama a la funcion para calcular el perimetro de un triangulo
tipo_actual = tipo_triangulo()
#Llama a la funcion para calcular el perimetro de un triangulo
print("El perimetro del triangulo es: ", calcular_perimetro(tipo_actual))