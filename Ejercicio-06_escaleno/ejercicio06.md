![headerDGTIC](/Imagenes/headerDGTIC.png)

##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 6

## Enunciado del problema
Programa que calcula el perímetro de un triángulo escaleno.

## Procedimiento 
1. Solicitar que se ingrese la longitud de cada uno de los lados del triángulo.
2. Calcular el perímetro del triángulo.
3. Mostrar el resultado.

## Entradas y salidas
#### Entradas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| Lado 1       |Longitud de un lado | float | 0 | Ninguno |
| Lado 2       |Longitud de un lado | float | 0 | Ninguno |
| Lado 3       |Longitud de un lado | float | 0 | Ninguno |

#### Salidas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| Perímetro       |Suma de los 3 lados| float | 0 | Ninguno |

#### Mensajes de salida
"El perímetro del triángulo escaleno de lados `lado1`, `lado2` y `lado3` es: `perimetro`"

## Diseño de la solución 
La solución se realizó de la siguiente forma:
#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocódigo
```plaintext
INICIO
    Solicitar la longitud de los 3 lados
        Verificar longitudes válidas
    Calcular el perímetro
    Mostrar el perímetro
FIN
```

## Código fuente
En el archivo **ejercicio06.py**
```python
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
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| Lado 1 = 5, Lado 2 = 6, Lado 3 = 2 | longitudes > 0 | perimetro = 13 | perimetro = 13 |
| Lado 1 = 0, Lado 2 = 6, Lado 3 = 5 | longitud cero | Lados de longitud inválida | Lados de longitud inválida |

![footerDGTIC](/Imagenes/footerDGTIC.png)