##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 8

## Enunciado del problema
Programa que calcula el perimetro de un triangulo escaleno.
Programa que recibe un numero e imprime la tabla de multiplicar de ese numero del 2 al 10

## Procedimiento 
1. Solicitar que se ingrese un numero.
2. MOstrar la tabla de multiplicar de ese numero

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
    INGRESAR NUMERO
    SI EL NUMERO ES VALIDO
    IMPRIMIR TABLA DE MULTIPLICAR DEL NUMERO DEL 2 AL 10
FIN
```

## Codigo fuente
En el archivo **ejercicio08.py**
```python
def hola_mundo():
    print("¡Hola, mundo!")
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| Lado 1 = 5, Lado 2 = 6, Lado 3 = 2 | longitudes > 0 | perimetro = 13 | perimetro = 13 |