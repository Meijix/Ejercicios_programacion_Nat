##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 3

## Enunciado del problema
Programa que recibe un monto en dolares y lo convierte a pesos.

## Procedimiento 
1. Solicitar que se ingrese un monto en dolares
2. Solicitar ingresar la tasa de cambio actual
3. Calcular el monto en pesos
4. Mostrar el monto en pesos


## Entradas y salidas
#### Entradas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| num  |Numero a considerar| int | 1 | Ninguno |

#### Salidas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| suma  | Suma de los numeros consecutivos hasta el numero ingresado | int | NA | NA

#### Mensajes de salida
- "La suma de sus consecutivos es: `suma`"
- "El número ingresado no es válido"

## Diseno de la solucion 
La solucion se realizo de la siguiente forma:
#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocodigo
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

#### Pruebas de escritorio
| Entrada | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|
| num = 10 | 55 |55 |