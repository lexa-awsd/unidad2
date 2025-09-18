lista = ["Mary", "Nicol", "Diego", "Alejandro"]
print (lista)
print (lista [2])
'''Añade un elemento al final de la lista.'''
lista.append("Alexa")
print (lista)
'''Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará'''
lista.insert(1,"lexa")
print (lista)
lista.pop()
print (lista)
'''Quita el primer ítem de la lista cuyo valor sea x'''
lista.remove("Nicol")
print (lista)
'''limina el elemento en la posición indicada en la lista y lo devuelve. 
Si no se especifica ningún índice, a.pop()elimina y devuelve el último elemento de la lista.'''
lista.pop(1)
print (lista)
