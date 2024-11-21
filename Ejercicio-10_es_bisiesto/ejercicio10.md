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
""

## Diseño de la solución 
La solucion se realizo de la siguiente forma:

#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocódigo
```plaintext
INICIO
    Solicitar año
    Verificar si es bisiesto
    Mostrar resultado
FIN
```

## Código fuente
En el archivo **ejercicio10.py**
```python
def es_bisiesto(año:int ) -> bool:
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True               
    else:
        return False
    
#Debe recibir el año a evaluar
año = int(input("Ingrese el año a evaluar: "))
#Llama a la función con el año ingresado
print(f"El año {año} es bisiesto?",es_bisiesto(año))  # Imprime True si el año es bisiesto
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| 2020 | Es bisiesto | True | True
| 2021 | No es bisiesto | False | False

![footerDGTIC](/Imagenes/footerDGTIC.png)