archivo = open('triangulo.txt', 'w')

a={}
while True:
    while True:
        try:
            for i in range(0,3):
                #absoluto en los numeros ingresados
               a[i]= int(input('ingrese lado de triangulo: '))
               a[i]= abs(a[i])
            break
        except:
            print('ingrese valores positivos')
            print('intente de nuevo')

    if a[0] == a[1] and a[1] == a[2]:
        print('triangulo equilatero')
        archivo.write('triangulo equilatero')
    elif a[0] != a[1] and a[0] != a[2] and a[1] != a[2]:
        print('triangulo escaleno')
        archivo.write('triangulo escaleno')
    else:
        print('triangulo iscoceles')
        archivo.write('triangulo iscoceles')

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