#Clases.py
#Aqui estan las clases modelo del sistema de Recomendaciones
#Marco Fuentes - 7 de mayo de 2019

from py2neo.ogm import *

class Persona(GraphObject):
	__primarykey__ = "nombre"

	nombre = Property()

	amigos = Related("Persona","amigos")
	likes = Related ("Atributo","likes")
	yaVisito = Related ("Ciudad","visitado")

class Ciudad (GraphObject):
	__primarykey__ = "nombre"

	nombre = Property()
	foto = Property()
	distancia = Property()
	contador = 0

class Atributo(GraphObject):
	__primarykey__ = "cualidad"

	cualidad = Property()
	#Lo pongo dos veces todo para que el recorrido sea bidireccional
	es = Related("Ciudad","ES")

class Pais (GraphObject):
	__primarykey__ = "nombre"

	nombre = Property()
	distancia = Property()
