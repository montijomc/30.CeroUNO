# Práctica 2
# Como te habrás dado cuenta, al ver el index de posts,
# y leer los datos, nos damos cuenta que el ID de los posts es incremental.
# Es decir, el primer post tiene el ID de 1, el segundo de 2
# y así consecutivamente hasta el 100.
# Y para accesar un ID de post debes pasarle ese número a posts así:
#  https://jsonplaceholder.typicode.com/posts/5
#
# Para poder accesar al post número 5.
# Escribe un iterador (for loop) que haga interpolación o concatenación de strings
# por la totalidad de los posts (son 100 posts).
# Debes concatenar el URL de index más los números del 1 al 100
# y haz un request para cada uno, e imprime el título del post.

import json
import requests

URL_inicial = 'https://jsonplaceholder.typicode.com/posts/'
my_request = requests.get(URL_inicial)
# convierto con ayuda de json el contenido de la pagina a una lista que esta compuesta de diccionarios
post_diccionario = json.loads(my_request.text)
for cadadiccionario in post_diccionario:  # obtengo cada diccionario de la lista
    # obtengo el valor del id de la tabla de post y lo convierto en string
    indice_del_post = str(cadadiccionario['id'])
    # concateno la ruta de lectura con el indice de los post
    URLpost = URL_inicial + indice_del_post
    print('URL DEL POST:', URLpost)
    my_request_URLpost = requests.get(URLpost)
    titulo_post = json.loads(my_request_URLpost.text)
    print('Post ', titulo_post['id'],':',titulo_post['title'])
    print()
