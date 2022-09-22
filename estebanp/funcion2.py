from array import array

def calcular(num):
    array = []
    cont = 0
    while(num != 0):
        temp = int(input("digitar temperatura"))
        array.append(temp)
        cont += 1
        if(cont == 2):
            contador = 0
            for i in array:
                contador= contador + i
                promedio = contador / 2
            print(promedio)
            break

calcular(1)