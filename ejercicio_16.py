# Obtener el menor numero de una lista cualquiera de números
l_num = [5, 8, 1, 45, 22, 21, 13]
menor = l_num[0]
for n in l_num:
    if (n < menor):
        menor = n
print ("La lista de números es: " + str (l_num))
print ("El menor valor de la lista es: " + str(menor))
