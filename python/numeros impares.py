archivo = open('numeros impares.txt', 'w')
while True:
    conteo=0
    for i in range(1, 101):
        if i%2 != 0:
            conteo=conteo+1
            print(f"{i} ")
            archivo.write(f"{i} ")
    print(f'existen {conteo} numeros impares')
    archivo.write(f'existen {conteo} numeros impares\n')
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