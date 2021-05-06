import tkinter as tk
from tkinter import *
import psycopg2
from psycopg2 import Error

# creando coneccion con postgres
try:
    conn = psycopg2.connect(
        host = "localhost" , 
        database = "problema3" ,
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

#funciones para los botones

def limpiar():
    #limpiar checkbox
    x.set(0)
    y.set(0)
    z.set(0)
    #limpiar cajas
    caja1.delete(0, tk.END)
    caja2.delete(0, tk.END)
    caja3.delete(0, tk.END)
    #limpiar radiobuuton
    radio1.deselect()
    radio2.deselect()
    radio3.deselect()

def salir():
        ventana.destroy()

def reporte():
    #para consulta de datos
        cursor.execute("SELECT *FROM vuelo")
        datos = cursor.fetchall()
        #print("subtotal,descuento,total")
       # print(datos)
        print('')
        print('')
        print('')
        print('')
        for columna in datos:
           print("************datos de consulta**************")
           print("id: # "+str(columna[3]))
           print("subtotal: Q "+str(columna[0]))
           print("descuento: Q "+str(columna[2]))
           print("total: Q "+str(columna[1]))
           

def calcular():
    #obtener la cantidad de servicios
    n1= num1.get()
    n2= num2.get()
    n3= num3.get()
    #verifica que clase de vuelo es
    op= clase1.get()
    variableDescuento = 0
    n1=0
    n2=0
    n3=0
    comida=0
    bebida=0
    pelicula=0
    if op==1: 
        if x.get()==1: #lectura de checkbox
            n1= num1.get()
            comida=50
        if y.get()==1:
            n2= num2.get()
            bebida=35
        if z.get()==1:
            n3= num3.get()
            pelicula=70
    elif op==2:
        if x.get()==1: #lectura de checkbox
            n1= num1.get()
            comida=40
        if y.get()==1:
            n2= num2.get()
            bebida=25
        if z.get()==1:
            n3= num3.get()
            pelicula=55
    elif op==3:
        if x.get()==1: #lectura de checkbox
            n1= num1.get()
            comida=25
        if y.get()==1:
            n2= num2.get()
            bebida=10
        if z.get()==1:
            n3= num3.get()
            pelicula=25
    else :
        print("*****************NO SELECCIONO NINGUN DATO*********************")

    subtotal= comida*n1 + bebida*n2 + pelicula*n3
    
    #calculo de descuento y total

    if n1+n2+n3 >10:    #descuento 1
        descuento = subtotal*0.1    #10%
        total = subtotal-descuento
        variableDescuento = 1

    if x.get()==1 and y.get()==1 and z.get()==1 and op==1 : #descuento 2
        descuento = subtotal*0.05   #5%
        total = subtotal-descuento
        variableDescuento = 1

    if x.get()==1 and y.get()==1 and z.get()==1 and op==1 and n1+n2+n3 >10:  #descuento 3
        descuento = subtotal*0.15   #15%
        total = subtotal-descuento
        variableDescuento = 1

    if variableDescuento==0:
        descuento=0
        total = subtotal

    print("")
    print("")
    print("**********************************")
    print(f"el subtotal es de Q {subtotal}")
    print(f"el descuento es de Q {descuento}")
    print(f"el total es de Q {total}")
    print("")
    print("")
    print("**********************************")

    #ingreso de datos a tabla vuelo(subtotal,descuento,total)
    try:
        cursor.execute("""INSERT INTO vuelo(subtotal,total,descuento) VALUES ('"""+str(subtotal)+"','"+str(total)+"','"+str(descuento)+"')")
        conn.commit()
        print("********************************************************************")
        print("******************actualizando base de datos************************")
        print("********************************************************************")
    except:
        print('***error al guardar datos en la BD')


#definir valores de la ventana
ventana = Tk()
ventana.geometry("600x600")
ventana['bg'] = '#49A'
ventana.title("aaron enrique ramirez palencia 201701022")

#variables
clase1 = IntVar()
x = IntVar()
y = IntVar()
z = IntVar()
num1 = IntVar()
num2= IntVar()
num3= IntVar()

#etiquetas
etiqueta1 = Label(ventana, text= '**CLASES DE VUELOS***')
etiqueta1.place(x=40,y=30)
etiqueta2 = Label(ventana, text= '**SERVICIOS ADQUIRIDOS***')
etiqueta2.place(x=350,y=30)

#cajas
caja1= Entry(ventana,textvariable=num1)
caja1.place(x=450,y=50)
caja2= Entry(ventana,textvariable=num2)
caja2.place(x=450,y=80)
caja3= Entry(ventana,textvariable=num3)
caja3.place(x=450,y=110)

#definir botones
BSalir = Button(ventana, text= "SALIR", command= salir)
BReporte = Button(ventana, text= "REPORTE", command= reporte)
BCalcular= Button(ventana, text= "CALCULAR", command= calcular)
BLimpiar = Button(ventana, text= "LIMPIAR", command= limpiar)

# posicion de botones
BLimpiar.place (x=10,y=550)
BSalir.place (x=100,y=550)
BReporte.place (x=200,y=550)
BCalcular.place (x=300,y=550)

#radio button
radio1 = Radiobutton(ventana,text=" 1era clase" ,value = 1, variable=clase1)
radio1.place(x=15,y=50)
radio2 = Radiobutton(ventana,text=" 2era clase" ,value = 2, variable=clase1)
radio2.place(x=15,y=80)
radio3 = Radiobutton(ventana,text=" 3era clase" ,value = 3, variable=clase1)
radio3.place(x=15,y=110)

#check box
checkComida = Checkbutton(ventana,text='comida',variable=x,
                            onvalue=1,
                            offvalue=0,)
checkComida.place(x=350,y=50)
checkBebida = Checkbutton(ventana,text='bebida',variable=y,
                            onvalue=1,
                            offvalue=0,)
checkBebida.place(x=350,y=80)
checkPelicula = Checkbutton(ventana,text='pelicula',variable=z,
                            onvalue=1,
                            offvalue=0,)
checkPelicula.place(x=350,y=110)


ventana.mainloop()
#cerrar coneccion
conn.close()