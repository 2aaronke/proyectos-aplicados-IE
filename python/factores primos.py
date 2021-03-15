def imprimir_factores_primos(numero):
    # Comience con dos, que es el primer primo
    factor = 2
    # Continúe hasta que el factor sea mayor que el número
    while factor <= numero:
    # Verificar si el factor es un divisor de número
        if not (numero % factor != 0):
            contador=0
            factores={}
            factores[contador]=factor
            mayor = factores[0]
            print(mayor)
            contador=contador+1
            for x in range(0, contador ):
                if factores[x] > mayor:
                    mayor = factores[x]
            numero /= factor
        else:
        # Si no es así, incremente el factor en uno
            factor += 1

    return 'listo'

imprimir_factores_primos(13195)
