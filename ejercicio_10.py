# Escribir un bucle que muestre los números pares del 0 al 40
num = 0
while (num < 40):
    num += 1
    if (num %2 == 0):
        print ("El número " + str(num) + " es par")
