#FUNCIONES EN PYTHON

def min_max(numeros):
    
    menor = numeros[0]
    mayor = numeros[0]
    
    for n in numeros:
        if n < menor:
            menor = n
            
        if n > mayor:
            mayor = n
    
    return menor, mayor


datos = [1,2,3,5,4,97,4,21,6,4,12,8,5,64,11,66,20,36,47,57]

print(min_max(datos))
#DECLARANDO FUNCIONES EN PYTHON 

def saludar(nombre):
    print(f'hola: {nombre}')
    
    
#utilizar o llamar funcion en python
saludar("Arian")
