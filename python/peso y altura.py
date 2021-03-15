#examen
import math
archivo = open('201701022.txt', 'w')
print('********MENU DE OPCIONES********')
while True:
    while True:
        try:
            print('1. altura y pesos')
            print('2. diferencia de suma de cuadrados')
            print('3. factores primos')
            print('4. sucesion fibonacci')
            print('5. areas y volumen')
            print('*************************')
            opcion =int(input('elegir el programa que desee ejecutar:  '))
            if opcion==1 or opcion==2 or opcion==3 or opcion==4 or opcion==5:
                break
        except:
            print('**ingrese una opcion valida del menu**')
            print('**intente de nuevo**')

    #primera opcion del menu
    if opcion==1:
        alturaMujeres=0
        alturaHombres=0
        alturapromedioMujeres=0
        alturapromedioHombres = 0
        pesoMujeres = 0
        pesoHombres = 0
        pesopromedioMujeres = 0
        pesopromedioHombres = 0
        contadorhombres=0
        contadormujeres=0
        n=int(input('numero de personas a evaluar:   '))
        for i in range(n):
            print('1. masculino')
            print('2. femenino')
            genero = int(input('seleccione la pocion de genero: '))
            altura = int(input('altura en metros: '))
            peso = int(input('peso en libras: '))
            if genero== 1:
                alturaHombres=alturaHombres+altura
                pesoHombres= pesoHombres+peso
                contadorhombres=contadorhombres+1
            if genero== 2:
                alturaMujeres=alturaMujeres+altura
                pesoMujeres= pesoMujeres+peso
                contadormujeres=contadormujeres+1
        pesopromedioHombres=(pesoHombres)/contadorhombres
        pesopromedioMujeres=(pesoMujeres)/contadormujeres
        alturapromedioHombres=(alturaHombres)/contadorhombres
        alturapromedioMujeres=(alturaMujeres)/contadormujeres
        print(f'el peso promedio de la poblacion masculina es de {pesopromedioHombres}')
        print(f'el peso promedio de la poblacion femenina es de {pesopromedioMujeres}')
        print(f'la altura promedio de la poblacion masculina es de {alturapromedioHombres}')
        print(f'la altura promedio de la poblacion femenina es de {alturapromedioMujeres}')
        archivo.write(f'el peso promedio de la poblacion masculina es de {pesopromedioHombres}\n')
        archivo.write(f'el peso promedio de la poblacion femenina es de {pesopromedioMujeres}\n')
        archivo.write(f'la altura promedio de la poblacion masculina es de {alturapromedioHombres}\n')
        archivo.write(f'la altura promedio de la poblacion femenina es de {alturapromedioMujeres}\n')

    # segunda opcion del menu
    if opcion == 2:
        sumaDecuadrados=0
        cuadradoDeSuma=0
        suma=0
        for i in range(100):
            sumaDecuadrados= sumaDecuadrados + math.pow(i+1,2)
        for i in range(101):
            suma=suma+i
        cuadradoDeSuma= math.pow(suma,2)
        resultado = cuadradoDeSuma-sumaDecuadrados
        print(f'la diferencia entre el cuadrado de la suma y suma de cuadrados es: {resultado}')
        archivo.write(f'la diferencia entre el cuadrado de la suma y suma de cuadrados es: {resultado}\n')

    # tercera opcion del menu
    if opcion == 3:
        def factoresPrimos(numero):
            factor = 2
            while factor <= numero:
                if not (numero % factor != 0):
                    print(factor)
                    numero /= factor
                else:
                    factor += 1
            return "ejecutado"
        factoresPrimos(600851475143)

    # cuarta opcion del menu
    if opcion == 4:
        print('serie de fibonacci')

    # quinta opcion del menu
    if opcion == 5:
        radio= int(input('ingrese el radio del cono: '))
        generatriz = int(input('ingrese la generatriz: '))
        alturacono = int(input('ingrese altura: '))
        areabase = math.pi*math.pow(radio,2)
        print(f'el area de la base es {areabase} m^2')
        archivo.write(f'el area de la base es {areabase} m^2\n')
        arealateral= math.pi*radio*generatriz
        print(f'el area lateral es {arealateral} m^2')
        archivo.write(f'el area lateral es {arealateral} m^2\n')
        areaTotal= areabase+arealateral
        print(f'el area total del cono es {areaTotal} m^2')
        archivo.write(f'el area total del cono es {areaTotal} m^2\n')
        volumen= (1/3)*math.pi*math.pow(radio,2)
        print(f'el volumen del cono es  {volumen} m^3')
        archivo.write(f'el volumen del cono es {volumen} m^3\n')


    #menu para volver a ejecutar el programa
    while True:
        try:
            print('1. SI')
            print('2. NO')
            seguir = int(input('desea continuar?: '))
            if seguir ==1 or seguir ==2:
                 break
        except:
            print('ingrese una opcion valida')
    if seguir == 2:
        break
print('gracias por su tiempo')
archivo.close()