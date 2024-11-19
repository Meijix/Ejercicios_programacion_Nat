##### Natalia Edith Mejia Bautista 
# Ejercicio 5
Programa que calcula el perimetro de un triangulo isoceles.


## Procedimiento 
1. Solicitar que se ingrese la longitud de uno de la basee y uno de los lados del triangulo.
2. Verificar longitudes mayores a cero.
3. Calcular el perimetro del triangulo.
4. Mostrar el resultado.

## Diagrama de actividad
![Diagrama de actividad 05](/Imagenes/Diagrama05.png)


## Pseudocodigo
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

## Codigo fuente
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