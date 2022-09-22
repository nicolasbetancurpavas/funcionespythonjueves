#El valle de aburra afronta altas temperaturas año tras año, Cree una que permita calcular la temperatura media de la tierra partir de recibir 20 datos diarios de temperatura.
#Daniel Ospina
temperaturas=[]

#función llenar arreglo temperaturas
def llenar(temperaturas):
    for i in range(20):
        temp=float(input(f"Ingrese la temperatura {i+1}: "))
        temperaturas.append(temp)

#función calcular media

def calcular(temperaturas):    
    llenar(temperaturas)
    suma=0
    media=0
    for temperatura in temperaturas:
        suma=suma + temperatura
    
    media=suma/len(temperaturas)

    return media

print(f'La temperatura media del Valle de Aburrá es: {calcular(temperaturas)}')

