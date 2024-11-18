##### Natalia Edith Mejia Bautista 
###### 16 noviembre, 2024

# Ejercicio 12

## Enunciado del problema
Programa que reciba un dia, mes y año y devuelva verdadero si la fecha es real y falso en caso contrario.
Debe tener en cuenta los años bisiestos.

## Procedimiento 
1. Solicitar que se ingrese una fecha
2. Validar que el ano sea mayor a 1
3. Validar que el mes sea mayor a 0 y menor o igual a 12
4. De acuerdo al mes corroborar que el dia sea valido, menor o igual a 30,31,28 o 20, segun sea el caso
5. Imprimir si la fecha es valida o no


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
En el archivo **ejercicio12.py**
```python
def es_bisiesto(año:int ) -> bool:
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True               
    else:
        return False

def es_fecha_real(dia, mes, año):
    status = True
    bisiesto = False
    
    #Verificar que es una fecha valida 
    cond_mes_invalid = (mes < 1 or mes > 12)
    cond_ano_invalid = (año < 1)

    if cond_ano_invalid:
        status = False
        print("Año inválido")

    if cond_mes_invalid:
        status = False
        print("Mes inválido")

    #Si el mes es febrero (2) se debe checar si el ano es bisiesto
    if mes == 2:
        if es_bisiesto(año)==True:
            bisiesto = True
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")

        #Si el año es bisiesto, febrero tiene 29 días
        if bisiesto==True:
            if dia < 1 or dia > 29:
                status = False
                print("Día inválido")
        #Si el año no es bisiesto, febrero tiene 28 días
        else:
            if dia < 1 or dia > 28:
                status = False
                print("Día inválido")
    #Si el mes es de 31 días
    elif mes in [1,3,5,7,8,10,12]:
        if dia < 1 or dia > 31:
            status = False
            print("Día inválido")
    #Si el mes es de 30 días
    else:
        if dia < 1 or dia > 30:
            status = False
            print("Día inválido")
    return status

year = int(input("Ingrese el año: "))
month = int(input("Ingrese el mes: "))
day = int(input("Ingrese el día: "))
print("Es fecha real?",es_fecha_real(day, month, year))
```

#### Pruebas de escritorio
| Entrada | Condiciones | Salida Esperada | Salida |
|:-------------:|:---------------:| :-------------:|:---------:|
| 2020, 2, 29 | Año bisiesto | True | True |
