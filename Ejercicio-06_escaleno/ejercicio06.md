##### Natalia Edith Mejia Bautista 
# Ejercicio 6
Programa que calcula el perimetro de un triangulo escaleno.


## Procedimiento 
1. Solicitar que se ingrese la longitud de cada uno de los lados del triangulo.
2. Calcular el perimetro del triangulo.
3. Mostrar el resultado.

## Entradas y salidas
| Valor  | **Tipo**  | Right Aligned |
|:------------- |:---------------:| -------------:|
| Row 1         | **Bold**        | Cell 3        |
| Row 2         | *Italic*        | Cell 6        |
| Row 3         | ~~Strike~~      | Cell 9        |
| Row 3         | [Link](dot.com) | Cell 9        |


## Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


## Pseudocodigo
```plaintext
INICIO
    Solicitar la longitud de los 3 lados
    Calcular el perimetro
    Mostrar el perimetro
FIN
```

## Codigo fuente
En el archivo **ejercicio06.py**
```python
def calcular_perimetro(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

#Debe recibir la longitud de la base y de los lados iguales
print("Perimetro de un triangulo escaleno")
lado1 = float(input("Ingrese la longitud del lado 1: "))
lado2 = float(input("Ingrese la longitud del lado 2: "))
lado3 = float(input("Ingrese la longitud del lado 3: "))
#Calcula el perimetro del triangulo isosceles
print(f"El perimetro del triangulo escaleno con lados {lado1},{lado2}, {lado3} es:", calcular_perimetro(lado1, lado2, lado3))
```