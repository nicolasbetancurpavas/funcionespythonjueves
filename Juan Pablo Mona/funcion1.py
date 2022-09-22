#FUNCIONES EN PYTHON

#Declarando funciones en python

from unittest import result


def saludar(nombre):
    print(f'Hola {nombre}')
    
# Utilizar una función
    
# saludar('Juan Pablo')

def calcular():
    datos = []
    i = 0
    while (i <= 20):
        dato = int(input("Porfavor ingrese un dato: "))
        datos.insert(i,dato)
        i = i + 1
    temperatura = 0
    for dato in datos:
        temperatura = dato + temperatura
    
    resultado = temperatura / 20
    
    print(resultado)

calcular()