##### Natalia Edith Mejia Bautista 
# Ejercicio 1
Escribir un programa que imprima los numeros pares del 0 al 100.

## Procedimiento 
1. Inicializar una variable para almacenar el número de inicio y final.
2. Inicializar un ciclo.
3. Verificar si es numero par.
4. Si es par, entonces imprimir. Si no lo es, seguir.
5. Incrementar el número actual en 1.
6. Repetir hasta llegar al 100.
7. Terminar.

##Entradas y salidas
| Left-Aligned  | Center Aligned  | Right Aligned |
|:------------- |:---------------:| -------------:|
| Row 1         | **Bold**        | Cell 3        |
| Row 2         | *Italic*        | Cell 6        |
| Row 3         | ~~Strike~~      | Cell 9        |
| Row 3         | [Link](dot.com) | Cell 9        |


## Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)
<!-- ![Logo de Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png) -->

<!-- Asi podemos hablar de `fun encontrar_pares`
Para imprimir **"¡Hola, mundo!"** en Python: -->

## Pseudocodigo
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