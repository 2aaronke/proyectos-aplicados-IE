
archivo = open('factorialMultiplo7.txt', 'w')

while True:
    resultado= 1
    while True:
        try:
            numero= int(input('ingrese un numero que sea multiplo de 7: '))
            if  numero % 7 == 0:
                break
        except:
            print("intente de nuevo****")
    for i in range(1,numero+1):
        resultado= i*resultado
    print(f'el factorial de {numero} es {resultado}')

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