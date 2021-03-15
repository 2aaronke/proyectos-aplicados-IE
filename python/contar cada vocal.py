archivo = open('contar cada vocal.txt', 'w')
while True:
    conteoA= 0
    conteoE = 0
    conteoI = 0
    conteoO = 0
    conteoU  = 0
    palabra = input("ingrese una palabra: ")
    for i in range(len(palabra)):
        if palabra[i] == 'a' or palabra[i] == 'A' or palabra[i] == 'á':
            conteoA= conteoA+ 1
        if palabra[i] == 'e' or palabra[i] == 'E' or palabra[i] == 'é':
            conteoE= conteoE+1
        if palabra[i] == 'i' or palabra[i] == 'I' or palabra[i] == 'í':
            conteoI= conteoI+1
        if palabra[i] == 'o' or palabra[i] == 'O' or palabra[i] == 'ó':
            conteoO= conteoO+1
        if palabra[i] == 'u' or palabra[i] == 'U' or palabra[i] == 'ú':
            conteoU= conteoU+1
    print(f'A = {conteoA}')
    print(f'E = {conteoE}')
    print(f'I = {conteoI}')
    print(f'O = {conteoO}')
    print(f'U = {conteoU}')
    archivo.write(f'A = {conteoA}\n')
    archivo.write(f'E = {conteoE}\n')
    archivo.write(f'I = {conteoI}\n')
    archivo.write(f'O = {conteoO}\n')
    archivo.write(f'U = {conteoU}\n')
    print('1. SI')
    print('2. NO')

    while True:
        try:
            seguir = int(input('desea continuar?: '))
            break
        except:
            print('ingrese una opcion valida')
    if seguir == 2:
        break
print('gracias por su tiempo')
archivo.close()