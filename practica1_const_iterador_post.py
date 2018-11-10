# Práctica 1
# Construye un iterador (for Loop) que consuma el índice de los posts
# https://jsonplaceholder.typicode.com/posts/
# e imprima todos los títulos de los posts.
# Por favor nota la estructura de datos:
# El índice es una lista de diccionarios,
# es decir, empieza con corchetes.
# El json.loads() será capaz de leerlo,
# pero para imprimir los datos debes tener esto en cuenta.

import json
import requests
# hago el requerimiento de la url a trabajar
my_request = requests.get('https://jsonplaceholder.typicode.com/posts')
# convertir el string del la pagina a tipo lista
my_req_dict = json.loads(my_request.text) # se convierte en lista compuesta de diccionarios
for idpost in my_req_dict:   # obtengo cada uno de los diccionarios de la lista
    print ('Titulo del post :',idpost['id'],':', idpost['title']) #imprimo la lista de los titulos de los posts
    print()
