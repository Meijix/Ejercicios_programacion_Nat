##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 14

## Enunciado del problema
Programa en el que el usuario debe adivinar un numero aleatorio entre 1 y 100
**Hint:** El programa debe mostrar si el numero ingresado es mayor o menor al numero a adivinar

- El programa debe mostrar cuantos intentos le tomo al usuario adivinar el numero
- El usuario solo tiene 5 intentos para adivinar el numero
- El programa debe mostrar un mensaje de GANASTE si el usuario adivina el numero
- El programa debe mostrar un mensaje de PERDISTE si el usuario no adivina el numero y el numero a adivinar


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
import random
numero_a_adivinar = random.randint(1, 100)
intentos = 0
print("Adivina el numero entre 1 y 100")
print("Tienes 5 intentos")
print("Buena suerte!")
while intentos < 5:
    intentos += 1
    numero_ingresado = int(input("Ingrese un numero: "))
    if numero_ingresado < numero_a_adivinar:
        print("Intenta un numero mayor")
    elif numero_ingresado > numero_a_adivinar:
        print("Intenta un numero menor")
    else:
        print(f"GANASTE! El numero a adivinar era {numero_a_adivinar}")
        print(f"Se necesitaron {intentos} intentos para adivinar el numero")
        break
else:
    print(f"PERDISTE! El numero a adivinar era {numero_a_adivinar}")
```

#### Pruebas de escritorio
**Numero a adivinar:** 86

| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| 50 | El numero ingresado es menor que el numero a adivinar | Intenta un numero mayor | Intenta un numero mayor |
| 70 | El numero ingresado es mayor que el numero a adivinar | Intenta 