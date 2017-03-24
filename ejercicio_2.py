# Escribir el algoritmo que, a partir de la cantidad de bancos de un aula y la cantidad de
# alumnos inscriptos para un curso, permita determinar si alcanzan los bancos existentes.
# De no ser así informar cuantos bancos sería necesario agregar.
cant_bancos = int(input("Ingrese la cantidad de bancos: "))
cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))
if (cant_bancos < cant_alumnos):
    cant_total = cant_alumnos - cant_bancos
    print ("Faltan " + str(cant_total) + "bancos.")
if (cant_bancos == cant_alumnos):
    print ("Cantidad suficiente de bancos.")
elif (cant_bancos > cant_alumnos):
    cant_total_2 = cant_bancos - cant_alumnos
    print ("Sobran " + str(cant_total_2) + " bancos.")
