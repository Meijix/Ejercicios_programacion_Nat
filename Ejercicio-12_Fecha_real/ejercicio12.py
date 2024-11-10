#Programa que reciba un dia, mes y año y devuelva verdadero si la fecha es real y falso en caso contrario.
#Debe tener en cuenta los años bisiestos.
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
print("Es fecha real?",es_fecha_real(day, month, year)) # Llama a la función con los valores ingresados por el usuario
