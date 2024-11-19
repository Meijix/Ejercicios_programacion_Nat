##### Natalia Edith Mejía Bautista 
###### 16 noviembre, 2024

# Ejercicio 3

## Enunciado del problema
Programa que recibe un monto en dólares y lo convierte a pesos.

## Procedimiento 
1. Solicitar que se ingrese un monto en dólares
2. Solicitar ingresar la tasa de cambio actual
3. Calcular el monto en pesos
4. Mostrar el monto en pesos


## Entradas y salidas
#### Entradas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `monto_dolares` | Monto en dólares | float | 0 | Ninguno |
| `tasa_cambio` | Tasa de cambio actual | float | 0 | Ninguno |

#### Salidas
| Nombre  | Descripción  | Tipo | Límite inferior | Límite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| `monto_pesos` | Monto en pesos | float | 0 | Ninguno |

#### Mensajes de salida
- "El monto en pesos es: `monto_pesos`"
- "El número ingresado no es válido"

## Diseño de la solución 
La solucion se realizo de la siguiente forma:
#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocodigo
```plaintext
Inicio
    Ingresar monto el dólares
        Verificar que es monto válido
    Ingresar tasa de cambio actual
        Verificar que es tasa de cambio válida
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
| monto_dolares = 45, tasa_cambio = 20.16 | El monto en pesos es: 907.2| El monto en pesos es: 907.2 |
| monto_dolares = 82.67, tasa_cambio = 19.61 | El monto en pesos es: 1621.1587 | El monto en pesos es: 1621.1587 |