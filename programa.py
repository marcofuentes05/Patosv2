#Sistema de Recomendaciones

#py2neo es un api para trabajar mejor con neo4j
from py2neo import *
#En Clases.py estan los modelos de objetos usados para el grafo en cada nodo.
from Clases import *
#pprint solo sirve para imprimir bonito
import pprint
#
import operator
#La contraseña es patos123


graph = Graph (password = "patos123")

nombre = input("Hola! Quien eres?\n")

persona = Persona()
persona.nombre = nombre

graph.pull(persona)

res =""
diccionario = {"prueba":1}

for amigo in persona.amigos:
    for c in amigo.yaVisito:
        res+= "Tu amigo "+ amigo.nombre + " estuvo en "+c.nombre+" /n"

for like in persona.likes:
    for c in like.es:
        if c.nombre in list(diccionario.keys()):
            diccionario[c.nombre] =+ 1
        else:
        	temp = {c.nombre:1}
        	diccionario.update(temp)
lista = list(diccionario.keys())
print(lista)
temp = 0
contador = 0
for i in lista:
    if diccionario[i] > temp:
        stra = lista[contador]
        contador+=contador
print("Tu ciudad ideal es: "+stra)
#para ordenar el DICCIONARIO
ordenado = sorted(diccionario.items(), key = operator.itemgetter(1))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(ordenado)