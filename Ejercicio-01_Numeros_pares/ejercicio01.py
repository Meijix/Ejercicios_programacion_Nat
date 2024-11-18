#Escribir un programa que imprima los numeros pares del 0 al 100.
start=0
end=100
print(f"Los numeros pares entre {start} y {end} son: ")
for i in range(start, end):
    #checar si es numero par
    if i % 2 == 0:
        print(i) 
