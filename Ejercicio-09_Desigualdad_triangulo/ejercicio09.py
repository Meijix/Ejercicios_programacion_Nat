#Teorema de la desigualdad del triangulo
#Si tienes tres segmentos de longitud a, b y c, entonces puedes formar un triángulo con ellos si y solo si se cumple la siguiente desigualdad:
# a + b > c & b + c > a & c + a > b

#Funcion que recibe la longitud de tres segmentos y determine si se puede formar un triángulo con ellos.
def es_triangulo(a, b, c):
    #Si se cumple la desigualdad del teorema de la desigualdad del triangulo
    return a + b > c and b + c > a and c + a > b

#Ejemplo
a = float(input("Ingrese la longitud del segmento a: "))
b = float(input("Ingrese la longitud del segmento b: "))
c = float(input("Ingrese la longitud del segmento c: "))
print("Es triangulo?", es_triangulo(a, b, c))  # Imprime True si se puede formar un triangulo con los segmentos dados, False en caso contrario
