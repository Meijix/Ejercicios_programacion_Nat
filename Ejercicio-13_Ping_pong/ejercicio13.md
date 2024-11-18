##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 12

## Enunciado del problema
### Ejercicio Ping Pong
Programa que imprime los numeros del 1 al 100. Pero con las siguientes condiciones:
- Para los multiplos de 3 imprime "ping" en lugar del numero 
- Para los multiplos de 5 imprime "pong" en lugar del numero. 
- Para los numeros que son multiplos de 3 y 5 imprime "ping pong" en lugar del numero.


## Procedimiento 
1. Solicitar que se ingrese una fecha
2. Validar que el ano sea mayor a 1
3. Validar que el mes sea mayor a 0 y menor o igual a 12
4. De acuerdo al mes corroborar que el dia sea valido, menor o igual a 30,31,28 o 20, segun sea el caso
5. Imprimir si la fecha es valida o no


## Entradas y salidas
#### Entradas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| numero | El numero ingresado por el usuario | int | 0 | 11 |

#### Salidas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| mes | Mes al que coresponde el numero | string | NA | NA |

#### Mensajes de salida
""

## Diseño de la solución 
La solucion se realizo de la siguiente forma:

#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocódigo
```plaintext
INICIO


FIN
```

## Código fuente
En el archivo **ejercicio13.py**
```python
def ping_pong():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("ping pong")
        elif i % 3 == 0:
            print("ping")
        elif i % 5 == 0:
            print("pong")
        else:
            print(i)

ping_pong()
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| 3 | Divisible entre 3 | "ping" | "ping" |
|4 | No divisible entre 3 y 5 | 4 | 4 |
| 5 | Divisible entre 5 | "pong" | "pong" |
| 15 | Divisible entre 3 y 5 | "ping pong" | "ping pong
