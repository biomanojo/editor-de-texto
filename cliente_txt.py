#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Inicio del programa
import menu
import json
import socket
import os
ruta_s = socket.socket()

#dirección ip del servidor
ruta_s.connect(("localhost", 35000))

while True:
    #demenu=menu.menu()
    #bmenu=json.loads(demenu)
   # menu.menu_lista(demenu)
    #print menu.hola()
    #mensaje = " "
    mensaje = raw_input('>>')
    ruta_s.send(mensaje)
    datos = ruta_s.recv(1024)

    if datos == "bienvenidos":
        print datos
        demenu = menu.menu()
        menu.menu_lista(demenu)
        opcion = raw_input("digite alguna opcion ")
        ruta_s.send(opcion)
        if opcion == 'a':

            dirname = "C:\\python27"
            mitexto = os.listdir(dirname)
            f = open("fichero.txt", 'w')
            for elemento in mitexto:
                print elemento
                f.write(elemento)
                f.write("\r\n")

            f.close()
            raw_input("Pulsa enter")
            demenu = menu.menu()
            menu.menu_lista(demenu)
            opcion = raw_input("digite alguna opcion ")
            ruta_s.send(opcion)
        if opcion == 'b':
            archivo= raw_input("nombre del archivo :")
            crear = open( archivo , 'w')
       # if archivo in crear :
            crear = open(archivo, 'w')
            crear = open(archivo, 'a')
            crear.write("holaa juaaa")
            #crear.write("hola juann\n")
            print "archivo creado",crear
            crear.close()
            raw_input("Pulsa enter")
            demenu = menu.menu()
            menu.menu_lista(demenu)
            opcion = raw_input("digite alguna opcion ")
            ruta_s.send(opcion)
        if opcion == 'c':
            editar=raw_input("archivo a modificar:")
            dirFichero = editar
            lineas = raw_input("ingreso de texto: ")
            fichero = open(dirFichero, 'a+')
            for l in lineas:
                fichero.write( l + '')
            fichero.close()
            raw_input("Pulsa enter")
            demenu = menu.menu()
            menu.menu_lista(demenu)
            opcion = raw_input("digite alguna opcion ")
            ruta_s.send(opcion)
        if opcion == 'd':
            eliminar= raw_input(" archivo a eliminar:")
            delete=os.remove(eliminar)
            print "archivo eliminado",delete
            raw_input("Pulsa enter")


        if mensaje == 'salir':
            break



print "Regrese Cuando Quiera"
#cerrar conexión con el servidor
ruta_s.close()
