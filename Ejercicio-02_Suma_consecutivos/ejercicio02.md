![headerDGTIC](/Imagenes/headerDGTIC.png)

##### Natalia Edith Mejía Bautista 
###### 16 noviembre, 2024

# Ejercicio 2

## Enunciado del problema
Programa que recibe un número de entrada entre 1 y 50 y suma los números consecutivos hasta llegar a ese número.

## Procedimiento 
1. Solicitar que se ingrese un número del 1 al 50.
2. Verificar si el número ingresado es válido (está entre el 1 y 50).
3. Si no lo es, imprimir "Número ingresado no válido".
4. Si es válido, sumar los números consecutivos hasta llegar al número ingresado e imprimir la suma.


## Entradas y salidas
#### Entradas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `num`  |Número a considerar| int | 1 | 50 |

#### Salidas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `suma`  | Suma de los números consecutivos hasta el número ingresado | int | NA | NA

#### Mensajes de salida
- "La suma de sus consecutivos es: `suma`"
- "El número ingresado no es válido"

## Diseño de la solución 
La solución se realizó de la siguiente forma:
#### Diagrama de actividad
![Diagrama de actividad 02](/Imagenes/Diagrama02.png)


#### Pseudocódigo
```plaintext
Inicio
    Leer num desde la entrada del usuario
    Mientras num>50 o num<1
        Imprimir "Número ingresado no válido"
    Fin Mientras

    Calcular la suma de sus consecutivos
        suma = 0
        Para i en el rango del 1 a num
            suma += i
            i += 1
        Fin Para
    Imprimir el resultado

Fin
```

## Código fuente
En el archivo **ejercicio02.py**
```python
def suma_consecutiva(numero):
    suma = 0
    for i in range(1, numero + 1):
        suma += i  
    return suma

num = int(input("Ingrese un número entre 1 y 50: "))
#Volver a solicitar el numero hasta que el usuario ingrese un numero valido.
while num < 1 or num > 50:
    print("El número ingresado no es válido")
    num = int(input("Ingrese un número entre 1 y 50: "))

print("La suma de sus consecutivos es:", suma_consecutiva(num))
```

#### Pruebas de escritorio
| Entrada | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|
| num = 10 | 55 |55 |
| num = 50 | 1275 |1275 |
| num = 100 | El número ingresado no es válido | El número ingresado no es válido |
| num = -2 | El número ingresado no es válido | El número ingresado no es válido |


![footerDGTIC](/Imagenes/footerDGTIC.png)