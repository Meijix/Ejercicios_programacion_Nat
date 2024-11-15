##### Natalia Edith Mejia Bautista 
# Ejercicio 3
Programa que recibe un monto en dolares y lo convierte a pesos.

## Procedimiento 
1. Solicitar que se ingrese un monto en dolares
2. Solicitar ingresar la tasa de cambio actual
3. Calcular el monto en pesos
4. Mostrar el monto en pesos

## Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


## Pseudocodigo
```plaintext
Inicio
    Ingresar monto el dolares
    Ingresar tasa de cambio actual
    Calcular monto en pesos 
    Imprimir resultado
Fin
```

## Codigo fuente
En el archivo **ejercicio03.py**
```python
def convertir_pesos(monto_dolares, tasa_cambio):
    monto_pesos = monto_dolares * tasa_cambio
    return monto_pesos

monto_dolares = float(input("Ingrese el monto en dolares: "))
tasa_cambio = float(input("Ingrese la tasa de cambio actual: "))
print("El monto en pesos es:", convertir_pesos(monto_dolares, tasa_cambio))
```