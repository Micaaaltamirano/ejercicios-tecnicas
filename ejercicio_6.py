# Diseñar un programa que permita al usuario cotizar valores en dólares y euros. Considerando que el dólar esta a $15.60
# y el euro a $17.90 , calcular el valor en pesos del monto ingresado por el usuario en la moneda seleccionada
dolar = 15.60
euro = 17.90
print ("Tipos de monedas a convertir: ")
print ("1) Dólares")
print ("2) Euros")
selec = int(input("Indique la opción correcta: "))
monto = float(input("Monto a convertir: "))
if (selec == 1):
    cotizacion_dolares = monto * 15.60
    print (str(monto) + " Dólares son $" + str(cotizacion_dolares))
else:
    cotizacion_euros = monto * 17.90
    print (str(monto) + " Euros son $" + str(cotizacion_euros))
