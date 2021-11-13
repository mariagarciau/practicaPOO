"""En el capítulo anterior, se han abordado las listas encadenadas.
¿Cómo modificar la estructura del elemento para transformarla en una clase
y añadir los métodos de gestión que permitan listar los elementos uno a uno,
en los dos sentidos, añadir un elemento, eliminarlo y volver al primero?
"""
miLista = [8,6,23,50,20,9,10,2,1,7,5]
print(miLista)
miLista.append(4)
print(miLista)
miLista.remove(6)
print(miLista)
print(max(miLista))
print(min(miLista))
print(len(miLista))
miLista.sort()
print(miLista)
