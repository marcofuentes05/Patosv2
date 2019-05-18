#Algoritmo 2 
#
from Clases import *
from py2neo import *
import pprint

graph = Graph (password = "patos123")

diccionario = {"prueba": 0}
nombre = input ("Hola! ¿Cual es tu nombre?\n")
des = input ("¿Que deseas que te recomiente?\n\t1. Un pais\n\t2. Una ciudad\n")
p = Persona()
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i].contador>alist[i+1].contador:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
p.nombre = nombre
listaLugares = []
graph.pull(p)
if (des == "1"):
	#Valoro los lugares visitados por los amigos
	for amigo in p.amigos:
		for p in amigo.yaVisitoP:
			if p in listaLugares:
				p.agregarC(3)
			else:
				lugar.contador = 0
				p.agregarC(3)
				listaLugares.append(p)
	#Y lo que le gusta a sus amigos
		"""for pref in amigo.likes:
			for lugar in pref.es:
				if lugar in listaLugares:
					lugar.agregarC(1)
				else:
					lugar.contador = 0
					lugar.agregarC(1)
					listaLugares.append(lugar)"""
	#Valoro los intereses del usuario
	for like in p.likes:
		for p in like.es:
			if p in listaLugares:	
				p.agregarC(5)
			else:
				lugar.contador = 0
				p.agregarC(5)
				listaLugares.append(p)

	bubbleSort(listaLugares)
	for i in listaLugares:
		print("\t"+i.nombre+" puntuacion: "+str(i.contador))

elif (des=="2"):

	for like in p.likes:
		for lugar in like.es:
			if lugar in listaLugares:
				lugar.agregarC(5)
			else:
				#lugar.contador = 0
				lugar.agregarC(5)
				listaLugares.append(lugar)

	for amigo in p.amigos:
		for p in amigo.yaVisito:
			if p in listaLugares:
				p.agregarC(3)
			else:
				#lugar.contador = 0
				p.agregarC(3)
				listaLugares.append(p)
		#Y lo que le gusta a sus amigos
		for pref in amigo.likes:
			for lugar in pref.es:
				if lugar in listaLugares:
					lugar.agregarC(1)
				else:
					#lugar.contador = 0
					lugar.agregarC(1)
					listaLugares.append(lugar)
	

	bubbleSort(listaLugares)
	listaLugares.reverse()
	for i in listaLugares:
		print("\t"+str(i.nombre)+" puntuacion: "+str(i.contador))
else:
	print("Ese valor no es valido :(")