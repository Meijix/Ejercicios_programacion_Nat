#Programa que recibe un año y determina si es bisiesto o no
def es_bisiesto(año:int ) -> bool:
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True               
    else:
        return False
    
#Debe recibir el año a evaluar
año = int(input("Ingrese el año a evaluar: "))
#Llama a la función con el año ingresado
print(f"El año {año} es bisiesto?",es_bisiesto(año))  # Imprime True si el año es bisiesto
