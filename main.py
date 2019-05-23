#------------------------------------------------------------
#proyecto.py
#Autores: Cristina Bautista, Andy Castillo, y Marco Fuentes
#Carnets: 161260, 18040,18188
#Fecha: Viernes 24 de mayo de 2019
#Descripción: Este programa usa una base de datos (grafo) de neo4j para recomendar ciudades o paises a usuarios para sus viajes
#------------------------------------------------------------

#Se importan las clases (modelo de datos)
from Clases import *
#Se importa la libreria que facilita la coneccion on neo4j: Py2Neo
from py2neo import *

#Version Adaptada de bubbleSort. Original de https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i].contador>alist[i+1].contador:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#Esta funcion nos permite saber si un lugar ya esta en la lista de recomendaciones o no.
#Devuelve un entero con la posicion del elemento, y -1 si no esta en la lista.
def estaEnLista(lista,nombre):
	for i in range(len(lista)):
		if lista[i].nombre == nombre:
			return i
	return -1

#La libreria reconoce el grafo de Neo4j, pero debemos especificarle la contraseña
graph = Graph (password = "patos123")

string = """
 /$$$$$$$$ /$$$$$$$  /$$$$$$ /$$    /$$  /$$$$$$   /$$$$$$   /$$$$$$
|__  $$__/| $$__  $$|_  $$_/| $$   | $$ /$$__  $$ /$$__  $$ /$$__  $$
   | $$   | $$  \ $$  | $$  | $$   | $$| $$  \ $$| $$  \__/| $$  \ $$
   | $$   | $$$$$$$/  | $$  |  $$ / $$/| $$$$$$$$| $$ /$$$$| $$  | $$
   | $$   | $$__  $$  | $$   \  $$ $$/ | $$__  $$| $$|_  $$| $$  | $$
   | $$   | $$  \ $$  | $$    \  $$$/  | $$  | $$| $$  \ $$| $$  | $$
   | $$   | $$  | $$ /$$$$$$   \  $/   | $$  | $$|  $$$$$$/|  $$$$$$/
   |__/   |__/  |__/|______/    \_/    |__/  |__/ \______/  \______/
"""
sigue0 = True
while sigue0:
    print(string)
    #Login (no es seguro, pero funciona bien) :D
    nombre = input ("Hola! ¿Cual es tu nombre? (Ingresa X para salir del programa)\n")
    #Hago esto para asegurarme que no voy a hacer pull de un objeto vacio
    d = graph.run("MATCH (n:Persona) WHERE n.nombre = '"+nombre+"' RETURN n").data()
    if len(d)>0:
        #Instancio una persona para que sirva de enlace entre mi programa y el grafo
        p = Persona()
        p.nombre = nombre
        #listaLugares tiene objetos Lugar
        graph.pull(p)
        sigue = True
        while sigue:
            #Viva la Libertad
            des1 = input("Hola, "+nombre+"\n\t1. Tus gustos \n\t2. Tus Amigos\n\t3. Sugerencia de Viaje\n\t4. Salir\n")
            if (des1 =="1"):
                for gusto in p.likes:
                    print(gusto.cualidad)
            elif(des1=="2"):
                for amigo in p.amigos:
                    print(amigo.nombre)
            elif(des1=="3"):
                    des = input ("¿Que deseas que te recomiente?\n\t1. Un pais\n\t2. Una ciudad\n")
                    listaLugares = []
                    if (des == "1"):
                    	#Valoro los intereses del usuario
                    	for like in p.likes:
                    		for pais in like.esP:
                    			numero = estaEnLista(listaLugares,pais.nombre)
                    			if (numero != -1):
                    				listaLugares[numero].sumar(5)
                    			else:
                    				temp = Lugar(pais.nombre)
                    				temp.sumar(5)
                    				listaLugares.append(temp)
                    	#Valoro los lugares visitados por los amigos
                    	for amigo in p.amigos:
                    		for paisito in amigo.yaVisitoP:
                    			numero = estaEnLista(listaLugares,paisito.nombre)
                    			if numero != -1:
                    				listaLugares[numero].sumar(3)
                    			else:
                    				temp = Lugar(paisito.nombre)
                    				temp.sumar(3)
                    				listaLugares.append(temp)
                    	bubbleSort(listaLugares)
                    	listaLugares.reverse()
                    	for i in listaLugares:
                    		print("\t"+i.nombre+" puntuacion: "+str(i.contador))

                    elif (des=="2"):
                    	#Lo que le gusta
                    	for like in p.likes:
                    		for lugar in like.es:
                    			numero = estaEnLista(listaLugares,lugar.nombre)
                    			if (numero != -1):
                    				listaLugares[numero].sumar(5)
                    			else:
                    				temp = Lugar(lugar.nombre)
                    				temp.sumar(5)
                    				listaLugares.append(temp)
                    	#Lo que sus amigos visitaron
                    	for amigo in p.amigos:
                    		for lugar in amigo.yaVisito:
                    			numero = estaEnLista(listaLugares,lugar.nombre)
                    			if numero != -1:
                    				listaLugares[numero].sumar(3)
                    			else:
                    				temp = Lugar(lugar.nombre)
                    				temp.sumar(3)
                    				listaLugares.append(temp)
                    		#Y lo que le gusta a sus amigos
                    		for pref in amigo.likes:
                    			for lugar in pref.es:
                    				numero = estaEnLista(listaLugares,lugar.nombre)
                    				if numero != -1:
                    					listaLugares[numero].sumar(1)
                    				else:
                    					tmp = Lugar (lugar.nombre)
                    					tmp.sumar(1)
                    					listaLugares.append(tmp)

                    	bubbleSort(listaLugares)
                    	listaLugares.reverse()
                    	for i in listaLugares:
                    		print("\t"+str(i.nombre)+" puntuacion: "+str(i.contador))
                    	print (str(len(listaLugares)))
                    else:
                    	print("Ese valor no es valido :(")
            elif(des1=="4"):
                sigue = False
                print("Hasta luego!")
            else:
                print("Ese no es un valor valido :(")
    elif(nombre=="X" or "x"):
        sigue0=False
        print("Adios ")
    else:
        print("Ese nombre no esta registrado :(")
