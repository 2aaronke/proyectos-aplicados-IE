archivo = open('conteo de vocales.txt', 'w')
while True:
    conteo = 0
    palabra = input("ingrese una palabra: ")
    for i in range(len(palabra)):
        if palabra[i] == 'a' or palabra[i]== 'e' or palabra[i]== 'i' or palabra[i]== 'o' or palabra[i]== 'u':
            conteo = conteo+1
    print(f"la palabra {palabra} tiene {conteo} vocales")
    archivo.write(f'la palabra {palabra} tiene {conteo} vocales\n')
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