#Clases.py
#Aqui estan las clases modelo del sistema de Recomendaciones
#Marco Fuentes - 7 de mayo de 2019

from py2neo.ogm import *

class Persona(GraphObject):
	__primarykey__ = "nombre"

	nombre = Property()
	edad = Property()
	nacionalidad = Property()

	amigos = Related("Persona")

class Ciudad (GraphObject):
	__primarykey__ = "nombre"

	nombre = Property()
	clima = Property()


class Atributo(GraphObject):
	__primarykey__ = "cualidad"

	cualidad = Property()
	#Lo pongo dos veces todo para que el recorrido sea bidireccional
	legusta = Related("Persona","LE_GUSTA")
	es = Related("Ciudad","ES")