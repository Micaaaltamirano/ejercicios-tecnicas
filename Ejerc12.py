# Pedir al usuario que ingrese 10 números, almacenarlos en un array y mostrarlos en pantalla al finalizar la carga.
num = 0
lista_10 = []
while (num < 10):
    numero = input("Ingrese un número: ")
    lista_10.append (numero)
    num +=1
print ("Los números ingresados son: " + str(lista_10))
