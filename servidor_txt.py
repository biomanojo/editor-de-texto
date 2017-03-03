#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Inicio del programa

import socket

#Crear una variable de conexión tipo socket
server = socket.socket()

#Dirección IP del servidor y puerto de conexión
server.bind(("", 35000))

#Cuantas conexiones se van a escuchar
server.listen(1)

#Si se recibe algo de la ruta acepta la conexión y almacena la dirección aceptada
ruta_c, direccion = server.accept()
#usuario='ok'
while True:
    #Tamaño de los mensajes enviados por el cliente

    recibido = ruta_c.recv(1024)
    #if usuario == recibido:
    #print "bienvedidos"

    mensaje = 'bienvenidos'
    ruta_c.send(mensaje)
    print "bienvenido : "
    if recibido == 'salir':
        break

    #imprimir la dirección IP del Cliente
    #print str(addr[0]) + "Envio: ", recibido

    #Devolver petición al cliente
    ruta_c.send(recibido)

print "Hasta la Vista!!! Baby"

#Cerrar ruta del cliente y servidor
ruta_c.close()
server.close()
