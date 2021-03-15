archivo = open('suma desde 1 a n.txt', 'w')
while True:
    resultado = 0
    while True:
        try:
            numero = int(input("ingrese un numero : "))
            break
        except:
            print('**ingrese un dato numerico**')
            print('**intente de nuevo **')
    for i in range(numero+1):
        resultado = resultado + i
    print(f'resultado {resultado}')
    archivo.write(f'resultado {resultado}\n')


    print('1. SI')
    print('2. NO')
    while True:
        try:
            seguir = int(input('desea continuar?: '))
            if seguir ==1 or seguir ==2:
                 break
        except:
            print('ingrese una opcion valida')
    if seguir == 2:
        break

print('gracias por su tiempo')
archivo.close()