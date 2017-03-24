# Diseñar un algoritmo que aplique un descuento del 10% al monto total de una
# compra si el pago es de contado.
print ("")
monto_compra = float(input("Ingrese el monto final de la compra: $"))
print ("")
print("Modos de pago: ")
print ("")
contado = print("1- Contado")
tarjetas = print("2- Con tarjeta débito/crédito")
print ("")
opc= int(input("Ingrese la opción correcta: "))
contado_desc = monto_compra - float(monto_compra *10 /100)
print ("")
if (opc == 1):
    print ("Obtuvo un 10% de descuento, su monto a pagar es: $" + str(contado_desc))
elif (opc == 2):
    print ("Su monto a pagar es: $" + str(monto_compra))
