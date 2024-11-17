##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 4

## Enunciado del problema
Programa que calcula el perimetro de un triangulo equilatero
Se pide al usuario que ingrese la longitud de un lado del triangulo.

## Procedimiento 
1. Solicitar que se ingrese la longitud de uno de los lados del triangulo.
2. Calcular el perimetro del triangulo.
3. Mostrar el resultado.


## Entradas y salidas
#### Entradas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| longitud_lado | longitud de un lado del triangulo | float | 0 | Ninguno  |

#### Salidas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| perimetro | perimetro del triangulo | float | 0 | Ninguno |

#### Mensajes de salida
- "El perimetro del triangulo equilatero con lados de longitud `long_lado` es: `perimetro`"
- "El número ingresado no es válido"

## Diseno de la solucion 
La solucion se realizo de la siguiente forma:
#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocodigo
```plaintext
INICIO
    Ingresar longitud_lado
        Verificar longitud valida
    Calcular perimetro
    Mostrar perimetro
FIN
```

## Codigo fuente
En el archivo **ejercicio04.py**
```python
def calcular_perimetro(lado):
    perimetro = lado * 3
    return perimetro

print("Perimetro de un triangulo equilatero")
long_lado = float(input("Ingrese la longitud de uno de los lados: "))
#Agregar comprobacion de que las longitudes no sean cero o negativos
print(f"El perimetro del triangulo equilatero con lados de longitud {long_lado} es:", calcular_perimetro(long_lado))
```

#### Pruebas de escritorio
| Entrada |Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:-------------:|
| 5 | Longitud entera | 15 | 15 |
| 10.2 | Longitud decimal | 30.6 | 30.6 |