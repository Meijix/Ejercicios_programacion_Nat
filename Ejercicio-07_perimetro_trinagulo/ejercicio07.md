![headerDGTIC](/Imagenes/headerDGTIC.png)

##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 7

## Enunciado del problema
Programa que calcula el peímetro de un triángulo.
Toma en cuenta el tipo de triángulo que es. Se pide al usuario que ingrese las entradas necesarias.

## Procedimiento 
1. Solicitar que se ingrese el tipo de triángulo.
2. Solicitar que se ingrese los lados del triángulo, dependiendo del tipo.
3. Calcular el perímetro del triángulo.
4. Mostrar el resultado.


## Entradas y salidas
#### Entradas
Las entradas dependen del tipo de triángulo elegido.

| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
|`tipo` | Tipo de triángulo | int | 1 | 3 |
| `lado1` |Longitud de un lado | float | 0 | Ninguno |
| `lado2` |Longitud de un lado (opcional) | float | 0 | Ninguno |
| `lado3`| Longitud de un lado (opcional) | float | 0 | Ninguno |

#### Salidas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `perimetro` |Suma de los 3 lados| float | 0 | Ninguno |

#### Mensajes de salida
El perímetro del triángulo de lados `lado1`, `lado2` y `lado3` es: `perimetro`

## Diseño de la solución 
La solución se realizó de la siguiente forma:

#### Diagrama de actividad

![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocódigo
```plaintext
Inicio
    Preguntar tipo de triangulo
        Verificar tipo válido
        Preguntar lados según tipo
        Calcular perímetro
    Mostrar resultado
Fin
```

## Código fuente
En el archivo **ejercicio07.py**
```python
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

tipo_actual = tipo_triangulo()
print("El perímetro del triángulo es: ", calcular_perimetro(tipo_actual))
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| tipo =3, lado1 = 5, lado2 = 6, lado3 = 2 | triángulo escaleno | perimetro = 13 | perimetro = 13 |
| tipo = 1, lado1 = 5 | triángulo equilátero | perimetro = 15 | perimetro = 15 |

![footerDGTIC](/Imagenes/footerDGTIC.png)