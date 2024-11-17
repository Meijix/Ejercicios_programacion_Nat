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
| monto_dolares | monto en dolares | float | 0 | Ninguno |
| tasa_cambio | tasa de cambio actual | float | 0 | Ninguno |

#### Salidas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| monto_pesos | monto en pesos | float | 0 | Ninguno |

#### Mensajes de salida
- "El monto en pesos es: `monto_pesos`"
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
if monto_dolares<=0:
    print("El número ingresado no es válido")
    else:
        pass

tasa_cambio = float(input("Ingrese la tasa de cambio actual: "))
if tasa_cambio<=0:
    print("El número ingresado no es válido")
    else:
        pass

print("El monto en pesos es:", convertir_pesos(monto_dolares, tasa_cambio))
```

#### Pruebas de escritorio
| Entrada | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|
| num = 10 | 55 |55 |