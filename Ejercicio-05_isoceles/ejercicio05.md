##### Natalia Edith Mejia Bautista 
# Ejercicio 5
Programa que calcula el perimetro de un triangulo isoceles.


## Procedimiento 
1. Solicitar que se ingrese la longitud de uno de la basee y uno de los lados del triangulo.
2. Calcular el perimetro del triangulo.
3. Mostrar el resultado.

## Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


## Pseudocodigo
```plaintext
INICIO
    Solicitar longitud_base
    Solicitar longitud_lado
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