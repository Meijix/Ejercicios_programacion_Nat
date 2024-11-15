##### Natalia Edith Mejia Bautista 
# Ejercicio 3
Programa que calcula el perimetro de un triangulo equilatero
Se pide al usuario que ingrese la longitud de un lado del triangulo.

## Procedimiento 
1. Solicitar que se ingrese la longitud de uno de los lados del triangulo.
2. Calcular el perimetro del triangulo.
3. Mostrar el resultado.

## Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


## Pseudocodigo
```plaintext
INICIO
    Ingresar longitud_lado
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
print(f"El perimetro del triangulo equilatero con lados de longitud {long_lado} es:", calcular_perimetro(long_lado))
```