# Diseñar un programa que solicite al operador un usuario. Los posibles nombres de usuario son "admin" y "operador".
# En caso de ser admin, se muestra la leyenda "Bienvenido Administrador", en caso de ser operador, "Bienvenido Operador", y
# en caso de ser otro usuario distinto, se muestra "Usuario desconocido". En caso de que el usuario haya ingresado admin u
# operador, se le solicita la contraseña, sino, se termina la ejecución.
admin_cont = "administrador1"
operador_cont = "operador1"
usuario = input("Ingrese su Nombre de Usuario: ")
if (usuario == "admin"):
    cont_admin = input("Bienvenido Administrador. Ingrese su contraseña: ")
    if (cont_admin == admin_cont):
        print ("Contraseña correcta.")
    else:
        print ("Contraseña incorrecta.")
elif (usuario == "operador"):
    cont_usuario = input("Bienvenido Operador. Ingrese su contraseña: ")
    if (cont_usuario == operador_cont):
        print ("Contraseña correcta.")
    else:
        print ("Contraseña incorrecta.")
else:
    print ("Usuario desconocido.")
