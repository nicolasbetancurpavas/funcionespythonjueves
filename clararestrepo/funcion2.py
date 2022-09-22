#Resto de función 

def calcularTemperatura():
    temperaturas = []
    for i in range(0,20,1):
        temperatura = int(input("Digite la temperatura de cada día: "))
        temperaturas.insert(i,temperatura)