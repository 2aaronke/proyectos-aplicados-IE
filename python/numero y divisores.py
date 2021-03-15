archivo = open('numero y divisores.txt', 'w')
while True:
    while True:
        try:
            numero = int(input("ingrese un numero: "))
            break
        except:
            print("**ingrese un dato numerico**")
            print("**intente de nuevo**")
    for i in range(1, numero + 1 ):
        if (numero % i) == 0:
            print(f"{i} ")
            archivo.write(f"{i} ")
    archivo.write("\n")
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
