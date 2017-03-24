# Diseñar un programa que solicite al operador un usuario y una contraseña, y que valide
# que esos datos sean correctos para permitir el ingreso al sistema

usuario = "profesor"
contraseña = "prof1"
ingreso = input("Ingrese su nombre de usuario: ")
if (ingreso == usuario):
    ingresocont = input("Ingrese su contraseña: ")
    if (ingresocont == contraseña):
        print ("Bienvenido profesor")
    else:
        print ("Usuario incorrecto")
else:
    print ("Usuario incorrecto")
