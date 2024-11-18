##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 10

## Enunciado del problema
Programa que recibe un año y determina si es bisiesto o no

## Procedimiento 
1. Solicitar que se ingrese un año
2. Comprobar si cumple la condicion
3. Imprimir boleano indicando si es bisiestos o no ese año.

## Entradas y salidas
#### Entradas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| año | Año a evaluar | int | 1 | 9999 |

#### Salidas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| bisiesto | Indicador de si el año es bisiesto | bool | NA | NA |

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
En el archivo **ejercicio10.py**
```python
def hola_mundo():
    print("¡Hola, mundo!")
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| Lado 1 = 5, Lado 2 = 6, Lado 3 = 2 | longitudes > 0 | perimetro = 13 | perimetro = 13 |