##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 1

## Enunciado del problema
Escribir un programa que imprima los numeros pares del 0 al 100.

## Procedimiento 
1. Inicializar una variable para almacenar el número de inicio y final.
2. Inicializar un ciclo.
3. Verificar si es numero par.
4. Si es par, entonces imprimir. Si no lo es, seguir.
5. Incrementar el número actual en 1.
6. Repetir hasta llegar al 100.
7. Terminar.

<!-- ## Entradas y salidas
| Left-Aligned  | Center Aligned  | Right Aligned |
|:------------- |:---------------:| -------------:|
| Row 1         | **Bold**        | Cell 3        |
| Row 2         | *Italic*        | Cell 6        |
| Row 3         | ~~Strike~~      | Cell 9        |
| Row 3         | [Link](dot.com) | Cell 9        |
 -->

 ## Entradas y salidas
#### Parametros
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| start  |Valor de inicio| int | 0 | Ninguno |
| end  |Valor de finalizacion| int | 0 | Ninguno |

#### Entradas
El programa no requiere que se ingresen valores.

#### Salidas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| Perimetro       |Suma de los 3 lados| float | 0 | Ninguno |

#### Mensajes de salida
El perimetro del triangulo de lados `lado1` es: `perimetro`

## Diseno de la solucion 
La solucion se realizo de la siguiente forma:
#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocodigo
<!-- ![Logo de Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png) -->

<!-- Asi podemos hablar de `fun encontrar_pares`
Para imprimir **"¡Hola, mundo!"** en Python: -->

```plaintext
Inicio
    Definir start = 0
    Definir end = 100
    
    Para i desde start hasta end - 1 hacer:
        Si i % 2 == 0 entonces
            Imprimir i
        FinSi
    FinPara
Fin
```

## Codigo fuente
En el archivo **ejercicio01.py**
```python
start=0
end=100

for i in range(start, end):
    if i % 2 == 0:
        print(i) 
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| Lado 1 = 5, Lado 2 = 6, Lado 3 = 2 | longitudes > 0 | perimetro = 13 | perimetro = 13 |