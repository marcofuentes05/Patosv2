""""
llenadoBD.py
Marco Fuentes - 18188
Menu basico y sencillo para llenar nuestra base de datos basada en grafos de Neo4J
Slu2
"""

#py2neo es un api para trabajar mejor con neo4j
from py2neo import *
#En Clases.py estan los modelos de objetos usados para el grafo en cada nodo.
from Clases import *
#pprint solo sirve para imprimir bonito
import pprint
graph = Graph (password = "stitch")

def agregarRelacion (n1, n2,relacion):
	d = graph.run("MATCH (n:Persona) WHERE n.nombre = '"+n1+"' RETURN n").data()
	if (len(d)>0):
		d1 = graph.run("MATCH (n:Persona) WHERE n.nombre = '"+n2+"' RETURN n").data()
		if (len(d1)>0):
			graph.run("MATCH (n:Persona),(m:Persona) WHERE n.nombre = '"+n1+"' AND m.nombre = '"+n2+"' CREATE (n)-[r:"+relacion+"]->(m) CREATE (m) -[l:"+relacion+"]-> (n) ")
			return True
		else:
			return False
	else:
		return False

def isInGraphPersona(nombre):
	d = graph.run("MATCH (n:Persona) WHERE n.nombre = '"+nombre+"' RETURN n").data()
	if (len(d)>0):
		return True
	else:
		return False
def isInGraphCiudad(nombre):
	d = graph.run("MATCH (n:Ciudad) WHERE n.nombre = '"+nombre+"' RETURN n").data()
	if (len(d)>0):
		return True
	else:
		return False
def isInGraphAtributo(c):
	d = graph.run("MATCH (n:Atributo) WHERE n.cualidad = '"+c+"' RETURN n").data()
	if (len(d)>0):
		return True
	else:
		return False

menu = """
	Menu
		1. Agregar Nodo de persona
		2. Agregar Nodo de Ciudad
		3. Agregar Nodo de Atributo
		4. Agregar Relación

"""

res = input(menu)


if (res == "1"):
	nombre = input("Ingresa el nombre de la persona")
	if (isInGraphPersona(nombre) == False):
		nacionalidad = input ("Ingresa la nacionalidad")
		edad = input ("Ingresa la edad")
		graph.run ("CREATE (n:Persona {nombre: '"+nombre+"', nacionalidad: '"+nacionalidad+"', edad :	 "+edad	+"})")
	else:
		print("Ese elemento ya esta en el grafo :D ")
elif (res == "2"):
	nombre = input("Ingresa el nombre de la ciudad")
	if (isInGraphCiudad(nombre) == False):
		graph.run ("CREATE (n:Ciudad {nombre: '"+nombre+"'})")
	else:
		print("Ese elemento ya esta en el grafo :D ")
elif (res == "3"):
	nombre = input("Ingresa el nombre del Atributo")
	if (isInGraphAtributo(nombre) == False):
		graph.run ("CREATE (n:Atributo {cualidad: '"+nombre+"'})")
	else:
		print("Ese elemento ya esta en el grafo :D ")
elif (res == "4"):
	n1 = input("Ingresa el nombre de la primera persona")
	n2 = input ("Ingresa el nombre de la segunda persona")
	relacion = input ("Ingresa el tipo de relacion")
	agregarRelacion(n1,n2,relacion)
else:
	print ("Ese no es un valor permitido")


#/*Agrega un nodo persona a la BD*/
#data = graph.run("MATCH (n:Persona) return n").data() #Retorna una lista de diccionarios con los elementos del grafo

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(data)
#print(len(data))

#nac = input("Ingresa una nacionalidad: \n")
#datos = graph.run("MATCH (n: Persona) WHERE n.nacionalidad = '"+nac+"' RETURN n.nombre").data()
#pp.pprint(datos)
#print ("Hay "+str(len(datos))+" personas con nacionalidad "+nac)

#Agregar una amistad

"""n1 = input("Ingresa el nombre de uno de los amigos: \n")
n2 = input ("Ingresa el nombre del otro amigo: \n")
amistad = "Amistad"""
#sePudo = agregarRelacion(n1,n2,amistad)
