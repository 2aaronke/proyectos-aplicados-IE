import psycopg2
from psycopg2 import Error

# creando coneccion con postgres
try:
    conn = psycopg2.connect(
        host = "localhost" , 
        database = "problema1" ,
        user= "postgres" , 
        password= "brasil",
        port = '5432'
        )
    print('             *********coneccion a BD realizada con exito**********')
except:
    print('****coneccion no se pudo realizar con exito****')

#Setting auto commit false
conn.autocommit = True

#crear cursor
cursor = conn.cursor()

#bucle para ingreso de datos
while True:

   

    while True:
        try:
            nombre = input("ingrese nombre del paciente:  ")
            break
        except:
            print('**ingrese un nombre valido')

    while True:
        try:
            edad = int(input('ingrese edad del paciente:  '))
            if edad > 0 and edad <= 100 :   #ingreso de datos correcto
                break
        except:
            print('ingrese una edad numerica y en a;os')

    while True:
        try:
            peso = int(input('ingrese peso del paciente en lb: ' ))
            if peso > 0 and peso <= 300 :  #ingreso de datos correcto
                break
        except:
            print('ingrese un peso correctamente')

    while True:
        try:
            altura = int(input('ingrese la altura del paciente en cm :  '))
            if altura > 0 and altura <= 300 :   #ingreso de datos correcto
                break
        except:
            print('ingrese una altura correcta')

    while True:
        print('****************************************************')
        print('-----------OPCIONES PARA LOS MESES------------------')
        print('1) ENERO           7)  JULIO')
        print('2) FEBRERO         8)  AGOSTO')
        print('3) MARZO           9)  SEPTIEMBRE' )
        print('4) ABRIL          10)  OCTUBRE')
        print('5) MAYO           11)  NOVIEMBRE')
        print('6) JUNIO          12)  DICIEMBRE')
        print('****************************************************')
        try:
            mes = int(input('mes de la cita:   '))
            if mes > 0 and mes <= 12 :   #ingreso de datos correcto
                break
        except:
            print('ingrese una opcion correcta para mes ')

    while True:
        print('****************************************************')
        try:
            dia = int(input('dia de la cita:   '))
            if dia > 0 and dia <= 31 :   #ingreso de datos correcto
                break
        except:
            print('ingrese una opcion correcta para dia ')
            
    while True:
        try:
            hora = int(input('ingrese la hora de la consulta en formato de 24H: '))
            if hora > 0 and hora <= 24 :   #ingreso de datos correcto
                break
        except:
            print('ingrese una hora en formato de 24H')
    
    fecha = '2021'+"/"+ str(mes) + "/" + str(dia)

    #ingreso de datos a tabla clinica(nombre,edad,peso,altura,fecha,hora)
    try:
        cursor.execute("""INSERT INTO clinica(nombre,edad,peso,altura,fecha,hora) VALUES ('"""+nombre+"','"+str(edad)+"','"+str(peso)+"','"+str(altura)+"','"+fecha+"','"+str(hora)+"')")
        conn.commit()
        print("********************************************************************")
        print("******************actualizando base de datos************************")
        print("********************************************************************")
    except:
        print('***error al guardar datos en la BD')
            
    print('')
    print('')
    print('')
    print('desea realizar consulta de citas segun un dias especifico?? ')
    print('**1. SI')
    print('**2. NO')
    while True:
        try:
            consulta= int(input('ingrese una opcion: '))
            if consulta== 1 or consulta== 2 :
                break
        except:
            print('ingrese una opcion valida')
            print('**1. SI')
            print('**2. NO')
    
    #consulta de citas
    if consulta==1 :
        while True:
            print('****************************************************')
            print('-----------OPCIONES MES DE CONSULTA------------------')
            print('1) ENERO           7)  JULIO')
            print('2) FEBRERO         8)  AGOSTO')
            print('3) MARZO           9)  SEPTIEMBRE' )
            print('4) ABRIL          10)  OCTUBRE')
            print('5) MAYO           11)  NOVIEMBRE')
            print('6) JUNIO          12)  DICIEMBRE')
            print('****************************************************')
            try:
                mesC = int(input('mes de la cita:   '))
                if mesC > 0 and mesC <= 12 :   #ingreso de datos correcto
                    break
            except:
                print('ingrese una opcion correcta para mes ')

        while True:
            print('****************************************************')
            try:
                diaC = int(input('dia de la cita:   '))
                if diaC > 0 and diaC <= 31 :   #ingreso de datos correcto
                    break
            except:
                print('ingrese una opcion correcta para dia ')
        
        #para consulta de datos
        fechaC= '2021'+"/"+ str(mesC) + "/" + str(diaC)
        cursor.execute("SELECT *FROM clinica where fecha = '"+fechaC+"'")
        datos = cursor.fetchall()
        #print("nombre,edad,peso,altura,fecha,hora")
       # print(datos)
        print('')
        print('')
        print('')
        print('')
        for columna in datos:
           print("************datos de consulta**************")
           print("nombre: "+columna[0])
           print("edad: "+str(columna[1])+"  a;os")
           print("peso: "+str(columna[2])+"  libras")
           print("altura: "+str(columna[3])+"  cm")
           print("fecha: "+str(columna[4])+"  formato a;o/mes/dia")
           print("hora: "+str(columna[5])+"  horas")
           

    #para repetir otro ingreso de datos
    print('')
    print('')
    print('')
    print('desea ingresar mas datos??')
    print('1. SI')
    print('2. NO')

    while True:
        try:
            seguir = int(input('desea continuar?: '))
            if seguir ==1 or seguir ==2:
                 break
        except:
            print('ingrese una opcion valida')
            print('1. SI')
            print('2. NO')
    if seguir == 2:
        break

print('************************************gracias por su tiempo***************************')
#cerrar coneccion
conn.close()