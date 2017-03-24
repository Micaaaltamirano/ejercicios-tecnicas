# Calcular el promedio de 5 notas ingresadas (notas del 1 al 10).
# Si el promedio es mayor a 7, aprobó la materia, sino reprobó.
lista_notas = []
cant_num = 0
while (cant_num < 5):
    nota = float(input ("Ingrese la nota obtenida por el alumno/a: "))
    if (nota > 0 and nota <= 10):
        lista_notas.append (nota)
        cant_num += 1
        suma = 0
        for n in lista_notas:
            suma = suma + n
        promedio = suma / 5
    else:
        print ("Deben ser notas del 1 al 10. Por favor, vuelva a intentarlo.")
print ("El promedio es: " + str(promedio))
aprobo = promedio >= 7 and promedio <= 10
desaprobo = promedio <= 6 and promedio >= 0
if (aprobo):
    print ("Alumno/a aprobado/a.")
else:
    print ("Alumno/a desaprobado/a")
