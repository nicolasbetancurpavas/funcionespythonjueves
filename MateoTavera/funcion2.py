#MATEO TAVERA RAMIREZ
def calcularTemperatura(dato, datos):        
    while dato < datos:
        dato += 1
        temperatura = int(input(f"Ingrese el {dato} dato: "))
        temperatura += temperatura
    media = temperatura / dato
    print(f"La media de la temperatura es {media}")

calcularTemperatura(0, 2)    


