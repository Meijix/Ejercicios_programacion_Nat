#Programa que calcula el perimetro de un triangulo
#Toma en cuenta el tipo de triangulo que es
# Se pide al usuario que ingrese las entradas necesarias, dependiendo del tipo de triangulo

#Funcion que dependiendo del numero de parametros va a calcular el perimetro de un triangulo
#Recibe los parametros necesarios para calcular el perimetro de un triangulo
def calcular_perimetro(opcion):
    #Triangulo equilatero
    if opcion == 1:
        long_lado = float(input("Ingrese la longitud de uno de los lados del triangulo equilatero: "))
        while long_lado <= 0:
            print("La longitud del lado debe ser mayor a 0")
            long_lado = float(input("Ingrese la longitud de uno de los lados del triangulo equilatero: "))
        perimetro = long_lado * 3

    #Triangulo isosceles
    elif opcion == 2:
        base = float(input("Ingrese la longitud de la base: "))
        while base <= 0:
            print("La longitud de la base debe ser mayor a 0")
            base = float(input("Ingrese la longitud de la base: "))
        lado = float(input("Ingrese la longitud de los lados iguales: "))
        while lado <= 0:
            print("La longitud de los lados iguales debe ser mayor a 0")
            lado = float(input("Ingrese la longitud de los lados iguales: "))
        perimetro = base + 2 * lado

    #Triangulo escaleno
    elif opcion == 3:
        lado1 = float(input("Ingrese la longitud del lado 1: "))
        while lado1 <= 0:
            print("La longitud del lado debe ser mayor a 0")
            lado1 = float(input("Ingrese la longitud del lado 1: "))

        lado2 = float(input("Ingrese la longitud del lado 2: "))
        while lado2 <= 0:
            print("La longitud del lado debe ser mayor a 0")
            lado2 = float(input("Ingrese la longitud del lado 2: "))

        lado3 = float(input("Ingrese la longitud del lado 3: "))
        while lado3 <= 0:
            print("La longitud del lado debe ser mayor a 0")
            lado3 = float(input("Ingrese la longitud del lado 3: "))
                                
        perimetro = lado1 + lado2 + lado3

    #Opcion invalida
    else:
        print("Opcion inválida")
        tipo_triangulo()
    return perimetro

#preguntar tipo de triangulo usando una funcion
def tipo_triangulo():
    print("Ingresa el número correspondiente a tu tipo de triángulo")
    print("1. Triángulo equilátero")
    print("2. Triángulo isoceles")
    print("3. Triángulo escaleno")
    opcion = int(input("Ingrese el tipo de triángulo: "))
    return opcion


#Llama a la funcion para calcular el perimetro de un triangulo
tipo_actual = tipo_triangulo()
#Llama a la funcion para calcular el perimetro de un triangulo
print("El perímetro del triángulo es: ", calcular_perimetro(tipo_actual))