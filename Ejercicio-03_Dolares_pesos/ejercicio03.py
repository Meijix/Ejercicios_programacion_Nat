#Programa que recibe un monto en dolares y lo convierte a pesos.
#Debe solicitar la tasa de cambio actual

def convertir_pesos(monto_dolares, tasa_cambio):

    #Convierte el monto en dolares a pesos
    monto_pesos = monto_dolares * tasa_cambio
    return monto_pesos


#Ejemplo de uso
monto_dolares = float(input("Ingrese el monto en dolares: "))
tasa_cambio = float(input("Ingrese la tasa de cambio actual: "))
print("El monto en pesos es:", convertir_pesos(monto_dolares, tasa_cambio))