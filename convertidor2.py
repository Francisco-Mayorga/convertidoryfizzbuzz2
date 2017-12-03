# -*- coding: utf-8 -*-

print "Bienvenido, vamos a crear un programa que convierta Kilómetros en Millas"

while True:
    print "Por favor ingrese el número de kilómetros que desea convertir"
    km = int(input("kilómetros: "))
    millas = km * 0.621371
    print(str(km) + " Kilómetros " + "equivalen a " + str(millas) + " Millas")
    print "¿quieres hacer otra conversión?"
    opciones = raw_input("pulse cualquier letra (sí) o N (no): ")
    if "N" == opciones.upper():
        print("¡Hasta la próxima!")
        break