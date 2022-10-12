numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def max_min(datos):
    mayor = datos[0]
    menor = datos[0]

    for n in datos:
        if (n < menor):
            menor = n
        if (n > mayor):
            mayor = n

    return print(f'numero menor: {menor} numero mayor:{mayor}')


max_min(numeros)
