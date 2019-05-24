# Sistema de Recomendaciones

En este repositorio se encuentra un sistema de recomendaciones de destinos de viajes turísticos usando una base de datos basada en un grafo.

Este sistema fue desarrollado para cumplir con el proyecto 2 de Estructuras de Datos, 2019.

## Base de Datos

Para poder usar nuestro pograma, es necesario tener la base de datos encendida y con los datos correctos. Los cyphers necesarios para llenar la base de datos a 300 nodos en total, suficientes para que el funcionamiento sea excelente, se encuentran en el archivo ```BaseDeDatos.txt```.

Basta con copiar y pegar todo el archivo en Neo4J Browser para que la base de datos ya esté completa.


## Software

Se usó Neo4J para realizar las tareas relacionadas con la creación y gestion de la base de datos de grafos.

Programación en Python 3

Para poder usar el programa, es necesario instalar py2neo usando Pip:

  ```pip install py2neo```
  
Ademas, la base de datos del proyecto ha de ser la única que esté abierta y la contraseña se especifica en las primeras lineas del programa. La contraseña de la base de datos usada para las pruebas es patos123.

El nombre del programa principal es ```main.py```. El archivo que almacena las clases (modelo de datos) ```Clases.py```.

## Algoritmos Usados

El algoritmo de recomendación implementado es una mezcla entre varios algoritmos de recomendación sencillos.

### Recomendación por gustos

	El algoritmo busca todos los lugares que cumplen con al menos una de las preferencias de viajes. 

### Recomendación por mis amigos

	El algoritmo busca las preferencias de los amigos del usuario, asi como tambien los lugares que ha visitado, y los agrega a la lista de recomendaciones

### Recomendacion ponderada

	Cada elemento en la lista de recomendaciones tiene un atributo contador, de manera que este contador se incrementa cada vez que ese destino aparece en la lista de recomendaciones. De esta forma, los lugares que cumplen con las preferencias del usuario tendran una ponderación mayor a los que no, pero que siguen en la lista.


## Datos
Cristina Bautista - Carné No. 161260

Andy Castillo - Carné No. 18040

Marco Fuentes - Carné No. 18188
