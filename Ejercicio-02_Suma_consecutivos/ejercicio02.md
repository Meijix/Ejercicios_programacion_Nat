##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 2

## Enunciado del problema
Programa que recibe un numero de entrada entre 1 y 50 y suma los numeros consecutivos hasta llegar a ese numero.

## Procedimiento 
1. Solicitar que se ingrese un numero del 1 al 50
2. Verificar si el numero ingresado es valido (esta entre el 1 y 50)
3. Si es valido, sumar los numeros consecutivos hasta llegar al numero ingresado e imprimir la suma.
4. Si no lo es, imprimir "Numero ingresado no valido"

 ## Entradas y salidas
#### Parametros
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| start  |Valor de inicio| int | 0 | Ninguno |
| end  |Valor de finalizacion| int | start+1 | Ninguno |

#### Entradas
El programa no requiere que se ingresen valores.

#### Salidas
Todos los numeros enteros pares entre `start` y `end`.
#### Mensajes de salida
"Los numeros pares entre `start` y `end` son: "

## Diseno de la solucion 
La solucion se realizo de la siguiente forma:
#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocodigo
```plaintext
Inicio
    Leer num desde la entrada del usuario   
    Verificar si num esta entre 1 y 50
        Imprimir la suma de sus consecutivos
    Sino
        Imprimir "El número ingresado no es válido"
    FinSi
Fin
```

## Codigo fuente
En el archivo **ejercicio02.py**
```python
def suma_consecutiva(numero):
    suma = 0
    for i in range(1, numero + 1):
        suma += i  
    return suma

num = int(input("Ingrese un numero entre 1 y 50: "))
if 1 <= num <= 50:
    print("La suma de sus consecutivos es:", suma_consecutiva(num))
else:
    print("El numero ingresado no es valido") 
```


#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| num = 10 |  | 55 |55 |