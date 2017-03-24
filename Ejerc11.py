# Escribir un programa que rellene un array con los números entre el 0 y 100 e imprima la lista en pantalla.
num = 0
lista = []
while (num <= 100):
    lista.append (num)
    num +=1
print ("Los números entre 0 y 100 son: " + str(lista))
