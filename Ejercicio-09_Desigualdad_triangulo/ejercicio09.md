##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 9

## Enunciado del problema
Programa que recibe la longitud de tres segmentos y determine si se puede formar un triángulo con ellos.

### Teorema de la desigualdad del triangulo
- Si tienes tres segmentos de longitud $$a, b,  c$$ , entonces puedes formar un triángulo con ellos si y solo si se cumple la siguiente desigualdad:
$$a + b > c,  b + c > a,  c + a > b$$

## Procedimiento 
1. Solicitar que se ingresen los valores de los lados a considerar.
2. Comprobar si la suma de dos lados cualesquiera es mayor que el tercer lado.
3. Imprimir boleano indicando si se puede formar un triángulo con los lados ingresados o no.


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

## Diseño de la solución 
La solucion se realizo de la siguiente forma:

#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocodigo
```plaintext
INICIO
    INGRESAR NUMERO
    SI EL NUMERO ES VALIDO
    IMPRIMIR TABLA DE MULTIPLICAR DEL NUMERO DEL 2 AL 10
FIN
```

## Codigo fuente
En el archivo **ejercicio09.py**
```python
def hola_mundo():
    print("¡Hola, mundo!")
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| Lado 1 = 5, Lado 2 = 6, Lado 3 = 2 | longitudes > 0 | perimetro = 13 | perimetro = 13 |

![footerDGTIC](/Imagenes/footerDGTIC.png)