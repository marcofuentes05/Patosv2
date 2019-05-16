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

#def isOnDatabase(personita)

jose = Persona()
jose.nombre = "jose"
jose.edad = 19
jose.nacionalidad = "Guatemalteco"

caro = Atributo()
caro.cualidad = "caro"

guatemala = Ciudad()
guatemala.nombre = "Guatemala"
guatemala.clima = "Calido"

caro.legusta.add(jose)
caro.es.add(guatemala)

graph.push(jose)
graph.push(caro)
graph.push(guatemala)

def agregarRelacion (n1, n2,relacion):
	d = graph.run("MATCH (n:Persona) WHERE n.nombre = '"+n1+"' RETURN n").data()
	if (len(d)>0):
		d1 = graph.run("MATCH (n:Persona) WHERE n.nombre = '"+n2+"' RETURN n").data()
		if (len(d1)>0):
			graph.run("MATCH (n:Persona),(m:Persona) WHERE n.nombre = '"+n1+"' AND m.nombre = '"+n2+"' CREATE (n)-[r:"+relacion+"]->(m) CREATE (m) -[l:"+relacion+"]-> (n) ")
			return True
		return False
	return False

#nombre = input("Ingresa el nombre de la persona")
#nacionalidad = input ("Ingresa la nacionalidad")
#edad = input ("Ingresa la edad")
#graph.run ("CREATE (n:Persona {nombre: '"+nombre+"', nacionalidad: '"+nacionalidad+"', edad :	 "+edad	+"})")

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
