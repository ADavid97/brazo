import time
import tkinter.messagebox
from tkinter import *
from pyfirmata import Arduino, SERVO

#----------------Pines PWM Arduino---------------------------------------
pinGDL1 = 3
pinGDL2 = 5
pinGDL3 = 6
pinGDL4 = 9
pinGLD5 = 10
pinGDL6 = 11
#-----------------------------------------------------------------------

placa = Arduino('COM3')

#-----------------Configurar pines en modo servo------------------------
placa.digital[pinGDL1].mode = SERVO
placa.digital[pinGDL2].mode = SERVO
placa.digital[pinGDL3].mode = SERVO
placa.digital[pinGDL4].mode = SERVO
placa.digital[pinGLD5].mode = SERVO
placa.digital[pinGDL6].mode = SERVO
#-----------------------------------------------------------------------




anguloAnterior = 0

def moverLentamente(angulo, pinGDL):
    global anguloAnterior
    if angulo >= anguloAnterior:
        for i in range(anguloAnterior, angulo + 1):
            placa.digital[pinGDL].write(i)
            time.sleep(0.015)
        anguloAnterior = angulo
    elif angulo < anguloAnterior:
        for i in range(anguloAnterior-angulo):
            anguloAnterior = anguloAnterior - 1
            placa.digital[pinGDL].write(anguloAnterior)
            time.sleep(0.015)
            if(anguloAnterior == angulo):
                 break

def validarEntrada(texto):#Esta funcion se va a encargar de validar si la entrada se trata de un numero, si es asi,regresara un valor verdadero, de lo contrario, regresara uno falso
    return texto.isdecimal()

def validarAngulo(angulo, maximo, minimo, pinGDL):#Esta funcion va a evitar que se envien angulos fuera del rango establecido por el programador
    if angulo >= minimo and angulo <= maximo:
        moverLentamente(angulo, pinGDL)
    else:
        tkinter.messagebox.showinfo(title="Advertencia", message="El angulo ingresado se encuentra fuera del rango")


#-------------------Funciones para mandar angulo a los pines------------
def GDL1 ():
    anguloS1 = int(registro1.get())
    #print(anguloS1)
    validarAngulo(anguloS1, 180, 0, pinGDL1)

def GDL2 ():
    anguloS2 = int(registro2.get())
    print(anguloS2)
    validarAngulo(anguloS2, 180, 0, pinGDL2)

def GDL3 ():
    anguloS3 = int(registro3.get())
    print(anguloS3)
    validarAngulo(anguloS3, 110, 70, pinGDL3)

def GDL4 ():
    anguloS4 = int(registro4.get())
    print(anguloS4)
    validarAngulo(anguloS4, 180, 0, pinGDL4)

def GDL5 ():
    anguloS5 = int(registro5.get())
    print(anguloS5)
    validarAngulo(anguloS5, 180, 0, pinGLD5)

def GDL6 ():
    anguloS6 = int(registro6.get())
    print(anguloS6)
    validarAngulo(anguloS6, 180, 0, pinGDL6)

#-----------------------------------------------------------------------

root = Tk()
root.geometry("300x400")
root.minsize(width=300, height=400)

#-----------------------Entrada GDL1----------------------------------
primerGDL = Label(root, text="Ingrese el angulo del primer GDL")
primerGDL.pack(anchor=W,padx=10)

registro1 = Entry(
    validate="key",
    validatecommand=(root.register(validarEntrada), "%S")
)
registro1.place(x=50, y=50, width=150)
registro1.pack()

botonDeConfirmacion1=Button(root, text='Girar GDL1', command=GDL1)
botonDeConfirmacion1.pack(anchor=W,padx=10)
#---------------------------------------------------------------------

#-----------------------Entrada GDL2----------------------------------
segundoGDL = Label(root, text="Ingrese el angulo del segundo GDL")
segundoGDL.pack(anchor=W, padx=10)

registro2 = Entry(
    validate="key",
    validatecommand=(root.register(validarEntrada), "%S")
)
registro2.place(x=50, y=100, width=150)
registro2.pack()

botonDeConfirmacion2 = Button(root, text='Girar GDL2', command=GDL2)
botonDeConfirmacion2.pack(anchor=W, padx=10)
#---------------------------------------------------------------------

#-----------------------Entrada GDL3----------------------------------
tercerGDL = Label(root, text="Ingrese el angulo del tercer GDL")
tercerGDL.pack(anchor=W, padx=10)

registro3 = Entry(
    validate="key",
    validatecommand=(root.register(validarEntrada), "%S")
)
registro3.place(x=50, y=150, width=150)
registro3.pack()

botonDeConfirmacion3 = Button(root, text="Girar GDL3", command=GDL3)
botonDeConfirmacion3.pack(anchor=W, padx=10)
#---------------------------------------------------------------------

#-----------------------Entrada GDL4----------------------------------
cuartoGDL = Label(root, text="Ingrese el angulo del cuarto GDL")
cuartoGDL.pack(anchor=W, padx=10)

registro4 = Entry(
    validate="key",
    validatecommand=(root.register(validarEntrada), "%S")
)
registro4.place(x=50, y=200, width=150)
registro4.pack()

botonDeConfirmacion4 = Button(root, text="Girar GDL4", command=GDL4)
botonDeConfirmacion4.pack(anchor=W, padx=10)
#---------------------------------------------------------------------

#-----------------------Entrada GDL5----------------------------------
quintoGDL = Label(root, text="Ingrese el angulo del quinto GDL")
quintoGDL.pack(anchor=W, padx=10)

registro5 = Entry(
    validate="key",
    validatecommand=(root.register(validarEntrada), "%S")
)
registro5.place(x=50, y=250, width=150)
registro5.pack()

botonDeConfirmacion5 = Button(root, text="Girar GDL5", command=GDL5)
botonDeConfirmacion5.pack(anchor=W, padx=10)
#---------------------------------------------------------------------

#-----------------------Entrada GDL6----------------------------------
sextoGDL = Label(root, text="Ingrese el angulo del sexto GDL")
sextoGDL.pack(anchor=W, padx=10)

registro6 = Entry(
    validate="key",
    validatecommand=(root.register(validarEntrada), "%S")
)
registro6.place(x=5, y=300, width=150)
registro6.pack()

botonDeConfirmacion6 = Button(root, text="Girar GDL6", command=GDL6)
botonDeConfirmacion6.pack(anchor=W, padx=10)
#---------------------------------------------------------------------

root.mainloop()