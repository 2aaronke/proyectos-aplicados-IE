archivo = open('numero inicio fin.txt', 'w')
while True:
    while True:
        try:
            num1 = int(input("ingrese un numero: "))
            num2 = int(input("ingrese un numero: "))
            break
        except:
            print("ingrese valor numerico")
            print("intente de nuevo")
    for i in range(num1 , num2 +1, 2):
        print(f"{i}")
        archivo.write(f"{i}, ")
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