"""Escriba una clase que permita describir un libro y situar los valores asociados.
Dar un ejemplo de uso en Python.
"""
class Libro():
    def __init__(self,titulo,nºpaginas,autor,editorial,fechaPublicacion,nºediciones):
        str:self.titulo = titulo
        int:self.nºpaginas = nºpaginas
        str:self.autor = autor
        str:self.editorial = editorial
        str:self.fechaPublicacion = fechaPublicacion
        int:self.nºediciones = nºediciones
libro1=Libro("Memorias de una salvaje",464,"Bebi Fernandez","Planeta","Noviembre 2018",10)

