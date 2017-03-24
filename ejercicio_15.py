# Obtener el mayor valor de una lista cualquiera de números
mayor = 0
l_num = [5, 8, 1, 45, 22, 21, 13]
for n in l_num:
    if (n > mayor):
        mayor = n
print ("La lista de números es: " + str (l_num))
print ("El mayor valor de la lista es: " + str(mayor))
