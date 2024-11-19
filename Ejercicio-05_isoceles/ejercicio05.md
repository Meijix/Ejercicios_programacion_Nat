![headerDGTIC](/Imagenes/headerDGTIC.png)

##### Natalia Edith Mejía Bautista 
###### 16 noviembre, 2024

# Ejercicio 5

## Enunciado del problema
Programa que calcula el perímetro de un triángulo isóceles.


## Procedimiento 
1. Solicitar que se ingrese la longitud de uno de la base y uno de los lados del triángulo.
2. Verificar longitudes mayores a cero.
3. Calcular el perímetro del triángulo.
4. Mostrar el resultado.


## Entradas y salidas
#### Entradas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `base` | longitud de la base | float | 0 | Ninguno |
| `lado` | Longitud de un lado del triángulo | float | 0 | Ninguno  |

#### Salidas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `perimetro` | Perímetro del triángulo | float | 0 | Ninguno |

#### Mensajes de salida
- "El perímetro del triángulo isóceles con base de longitud `base` y lados iguales de longitud `lado` es: `perimetro` "
- "El número ingresado no puede ser negativo"
- "Ingrese una longitud válida: "

## Diseño de la solución 
La solución se realizó de la siguiente forma:
#### Diagrama de actividad
![Diagrama de actividad 05](/Imagenes/Diagrama05.png)


#### Pseudocódigo
```plaintext
INICIO
    Solicitar longitud_base
        Verificar longitud valida
    Solicitar longitud_lado
        Verificar longitud valida
    Calcular perimetro
    Mostrar perimetro
FIN
```

## Código fuente
En el archivo **ejercicio05.py**
```python
def calcular_perimetro(base, lado):
    perimetro = base + 2 * lado
    return perimetro
print("Perimetro de un triangulo isosceles")
base = float(input("Ingrese la longitud de la base: "))
lado = float(input("Ingrese la longitud de los lados iguales: "))
#Calcula el perimetro del triangulo isosceles
print(f"El perimetro del triangulo isosceles con base de longitud {base} y lados iguales de longitud {lado} es:", calcular_perimetro(base, lado))
```

#### Pruebas de escritorio
| Entrada |Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:-------------:|
| base = 5, lado = 6 | Longitudes enteras | 17 | 17 |
| base = 10.2, lado = 5.5 | Longitudes decimales | 21.2| 21.2 |

![footerDGTIC](/Imagenes/footerDGTIC.png)