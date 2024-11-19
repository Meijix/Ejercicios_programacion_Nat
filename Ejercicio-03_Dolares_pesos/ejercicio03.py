#Programa que recibe un monto en dolares y lo convierte a pesos.
#Debe solicitar la tasa de cambio actual

def convertir_pesos(monto_dolares, tasa_cambio):

    #Convierte el monto en dolares a pesos
    monto_pesos = monto_dolares * tasa_cambio
    return monto_pesos


#Solicita el monto en dolares y la tasa de cambio
monto_dolares = float(input("Ingrese el monto en dólares: "))
while monto_dolares < 0:
    print("El monto no puede ser negativo")
    monto_dolares = float(input("Ingrese el monto en dólares: "))
tasa_cambio = float(input("Ingrese la tasa de cambio actual: "))
while tasa_cambio < 0:
    print("La tasa de cambio no puede ser negativa")
    tasa_cambio = float(input("Ingrese la tasa de cambio actual: "))
#Imprime el monto en pesos
print("El monto en pesos es:", convertir_pesos(monto_dolares, tasa_cambio))