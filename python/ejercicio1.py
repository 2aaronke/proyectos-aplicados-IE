#PEDIR NUMEROS
#creando un vector vacio
a = {}
archivo = open('ejercicio1.txt', 'w')
while True:
    while True:
        try:
            for i in range(0,3):
                a[i] = int(input('ingrese un  numero : '))
            break
        except:
            print("**valores ingresados incorrectos**")
            print("**ingrese valores nuevamente**")

    #el primer numero es mayor
    if a[0] > a[1] and a[0] > a[2]:
        archivo.write(f'la suma de los tres numeros es {a[0]+a[1]+a[2]}\n')
        print(f'la suma de los tres numeros es {a[0]+a[1]+a[2]}')
    #el segundo numero es mayor
    if a[1]> a[0] and a[1]> a[2]:
       archivo.write(f'la multiplicacion de los tres numeros es : {a[0]*a[1]*a[2]}\n')
       print(f'la multiplicacion de los tres numeros es : {a[0]*a[1]*a[2]}')
    #el tercer numero es mayor
    if a[2]> a[0] and a[2]> a[1]:
        archivo.write(f'los tres numeros son : {a[0]}{a[1]}{a[2]}\n')
        print(f'los tres numeros son : {a[0]}{a[1]}{a[2]}')
    #los 3 numeros son iguales
    if a[0]==a[1]==a[2]:
        archivo.write('TODOS SON IGUALES')
        print(f'TODOS SON IGUALES')
    #2 numeros repetidos
    if a[0]==a[1]:
        if a[2]!= a[0]:
            archivo.write(f'numero unico: {a[2]}\n')
            print(f'numero unico: {a[2]}')
    if a[0]==a[2]:
        if a[1]!= a[0]:
           archivo.write(f'numero unico: {a[1]}\n')
           print(f'numero unico: {a[1]}')
    if a[1]==a[2]:
        if a[0]!= a[1]:
           archivo.write(f'numero unico: {a[0]}\n')
           print(f'numero unico: {a[0]}')
    print("desea ingresar datos nuevamente?")
    print("1. SI")
    print("2. NO")
    while True:
        try:
            seguir = int(input("selecione la opcion con un numero: "))
            break
        except:
            print("**ingrese una opcion valida**")
    if seguir==2:
        break
print("***GRACIAS POR PARTICIPAR***")
archivo.close()