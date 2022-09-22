#MATEO TAVERA RAMIREZ
def calcularTemperatura():    
    datos = 2
    dato = 0
    
    while dato < datos:
        dato += 1
        temperatura = int(input(f"Ingrese el {dato} dato: "))
        temperatura += temperatura
    media = temperatura/dato
    print(f"La media de la temperatura es {media}")

calcularTemperatura()    


