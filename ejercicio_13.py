# Almacenar 5 números por teclado y mostrar el promedio de ellos.
num = 0
lta_nro = []
while (num < 5):
    number = int(input("Ingrese un número: "))
    lta_nro.append(number)
    num += 1
numero = 0
for n in lta_nro:
    numero = numero + n
promedio = numero / 5
print ("El promedio de los números ingresados es: " + str(promedio))
