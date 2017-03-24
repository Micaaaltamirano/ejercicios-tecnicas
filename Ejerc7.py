# Crear una calculadora. El usuario deberá ingresar un valor, luego una
# operación (1 para sumar, 2 para restar, 3 para dividir, 4 para multiplicar) y
# un segundo valor para completar el calculo. El sistema deberá mostrar el resultado.
print ("CALCULADORA")
print ("")
v1= float(input("Ingrese un valor: "))
print ("Operaciones a realizar: ")
print ("1) SUMAR")
print ("2) RESTAR")
print ("3) DIVIDIR")
print ("4) MULTIPLICAR")
operac = int(input("Ingrese la opción que necesita realizar: "))
v2= float(input("Ingrese un segundo valor: "))
if (operac == 1):
    print ("El resultado es: " + str(v1 + v2))
elif (operac == 2):
    print ("El resultado es: " + str(v1 - v2))
elif (operac == 3):
    print ("El resultado es :" + str(v1 / v2))
elif (operac == 4):
    print ("El resultado es: " + str(v1 * v2))
else:
    print ("Opción incorrecta")
