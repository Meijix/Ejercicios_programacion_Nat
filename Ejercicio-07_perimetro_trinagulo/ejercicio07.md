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
```python
def hola_mundo():
    print("¡Hola, mundo!")
```

## Código fuente
En el archivo **ejercicio07.py**

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| tipo =3, lado1 = 5, lado2 = 6, lado3 = 2 | triángulo escaleno | perimetro = 13 | perimetro = 13 |
| tipo = 1, lado1 = 5 | triángulo equilátero | perimetro = 15 | perimetro = 15 |

![footerDGTIC](/Imagenes/footerDGTIC.png)