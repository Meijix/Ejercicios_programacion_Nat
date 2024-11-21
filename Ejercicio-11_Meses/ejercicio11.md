##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 11

## Enunciado del problema
Programa que recibe un numero entero entre 0 y 11 y muestra el mes correspondiente

## Procedimiento 
1. Solicitar que se ingrese un numero entre 0 y 11.
2. Verificar que el numero ingresado es valido. Si no, imprimir que no es valido ese numero.
3. Mostrar el mes correspondiente al numero ingresado. 


## Entradas y salidas
#### Entradas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| numero | El numero ingresado por el usuario | int | 0 | 11 |

#### Salidas
| Nombre  | Descripcion  | Tipo | Limite inferior | Limite superior |
|:-------------:|:---------------:| :-------------:|:---------:|:---------:|
| mes | Mes al que coresponde el numero | string | NA | NA |

#### Mensajes de salida
""

## Diseño de la solución 
La solucion se realizo de la siguiente forma:

#### Diagrama de actividad
![Ejemplo de imagen](https://ejemplo.com/imagen.png)


#### Pseudocódigo
```plaintext
INICIO
    INGRESAR NUMERO
    SI EL NUMERO ES VALIDO
        MOSTRAR EL MES CORRESPONDIENTE AL NUMERO
    FIN SI
FIN
```

## Código fuente
En el archivo **ejercicio11.py**
```python
#Arreglo con los nombres de los meses ordenados
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

numero = int(input("Ingrese un numero entero entre 0 y 11: "))
if 0 <= numero <= 11:
    print(meses[numero])
else:
    print("El numero ingresado no es valido")
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| 0 | Numero valido | Enero | Enero |
| 11 | Numero valido| Diciembre | Diciembre |
| 15 | Numero superior al limite | El numero ingresado no es valido | El numero ingresado no es valido |
| -2 | Numero negativo | El numero ingresado no es valido |El numero ingresado no es valido |

![footerDGTIC](/Imagenes/footerDGTIC.png)