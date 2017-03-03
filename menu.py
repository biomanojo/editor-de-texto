#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
def menu():
    lista=['a.Listar Archivo','b.Crear Archivo','c.Modificar Archivo','d.Eliminar Archivo','e.salir']
    datos=json.dumps(lista)
    return datos
def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def hola():
    print "hola mundo"
