![headerDGTIC](/Imagenes/headerDGTIC.png)

##### Natalia Edith Mejía Bautista 
###### 16 noviembre, 2024

# Ejercicio 4

## Enunciado del problema
Programa que calcula el perímetro de un triángulo equilátero.
- Se pide al usuario que ingrese la longitud de un lado del triángulo.

## Procedimiento 
1. Solicitar que se ingrese la longitud de uno de los lados del triángulo.
2. Calcular el perímetro del triángulo.
3. Mostrar el resultado.


## Entradas y salidas
#### Entradas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `longitud_lado` | longitud de un lado del triangulo | float | 0 | Ninguno  |

#### Salidas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `perimetro` | Perímetro del triángulo | float | 0 | Ninguno |

#### Mensajes de salida
- "El perímetro del triángulo equilátero con lados de longitud `longitud_lado` es: `perimetro`"
- "El número ingresado no es válido"

## Diseño de la solución 
La solución se realizó de la siguiente forma:
#### Diagrama de actividad
![Diagrama de actividad 04](/Imagenes/Diagrama04.png)


#### Pseudocódigo
```plaintext
INICIO
    Ingresar longitud_lado
        Verificar longitud válida
    Calcular perímetro
    Mostrar perímetro
FIN
```

## Código fuente
En el archivo **ejercicio04.py**
```python
def calcular_perimetro(lado):
    perimetro = lado * 3
    return perimetro

print("Perimetro de un triangulo equilatero")
#Ingresa la longitud de uno de los lados del triangulo equilatero
longitud_lado = float(input("Ingrese la longitud de uno de los lados del triangulo equilatero: "))
while longitud_lado < 0:
    print("La longitud del lado no puede ser negativa")
    longitud_lado = float(input("Ingrese una longitud válida: "))
print(f"El perímetro del triángulo equilátero con lados de longitud {longitud_lado} es:", calcular_perimetro(longitud_lado))
```

#### Pruebas de escritorio
| Entrada |Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:-------------:|
| 5 | Longitud entera | 15 | 15.0 |
| 10.2 | Longitud decimal | 30.6 | 30.599999999999998 |


![footerDGTIC](/Imagenes/footerDGTIC.png)