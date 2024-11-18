##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 14

## Enunciado del problema
Programa en el que el usuario debe adivinar un numero aleatorio entre 1 y 100
Hint: El programa debe mostrar si el numero ingresado es mayor o menor al numero a adivinar
El programa debe mostrar cuantos intentos le tomo al usuario adivinar el numero
El usuario solo tiene 5 intentos para adivinar el numero
El programa debe mostrar un mensaje de GANASTE si el usuario adivina el numero
El programa debe mostrar un mensaje de PERDISTE si el usuario no adivina el numero y el numero a adivinar


## Procedimiento 
1. 

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
