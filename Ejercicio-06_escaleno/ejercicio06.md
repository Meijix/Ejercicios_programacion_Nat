##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 6

## Enunciado del problema
Programa que calcula el perimetro de un triangulo escaleno.


## Procedimiento 
1. Solicitar que se ingrese la longitud de cada uno de los lados del triangulo.
2. Calcular el perimetro del triangulo.
3. Mostrar el resultado.

## Entradas y salidas
#### Entradas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| Lado 1       |Longitud de un lado | float | 0 | Ninguno |
| Lado 2       |Longitud de un lado | float | 0 | Ninguno |
| Lado 3       |Longitud de un lado | float | 0 | Ninguno |

#### Salidas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| Perimetro       |Suma de los 3 lados| float | 0 | Ninguno |

#### Mensajes de salida
El perimetro del triangulo de lados `lado1`, `lado2` y `lado3` es: `perimetro`

## Diseno de la solucion 
La solucion se realizo de la siguiente forma:
#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocodigo
```plaintext
INICIO
    Solicitar la longitud de los 3 lados
        Verificar longitudes validas
    Calcular el perimetro
    Mostrar el perimetro
FIN
```

## Codigo fuente
En el archivo **ejercicio06.py**
```python
def calcular_perimetro(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

#Debe recibir la longitud de la base y de los lados iguales
print("Perimetro de un triangulo escaleno")
lado1 = float(input("Ingrese la longitud del lado 1: "))
lado2 = float(input("Ingrese la longitud del lado 2: "))
lado3 = float(input("Ingrese la longitud del lado 3: "))
#Calcula el perimetro del triangulo isosceles
print(f"El perimetro del triangulo escaleno con lados {lado1},{lado2}, {lado3} es:", calcular_perimetro(lado1, lado2, lado3))
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| Lado 1 = 5, Lado 2 = 6, Lado 3 = 2 | longitudes > 0 | perimetro = 13 | perimetro = 13 |