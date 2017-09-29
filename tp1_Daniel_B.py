#Glosario
"""
VB = Ventana de Bloqueo
CB = Canvas de Bloqueo
VP = Ventana Principal
CP = Canvas Principal
"""
#Bibliotecas
from tkinter import *
from tkinter import messagebox
import time
from threading import Thread
import threading
import os
#Globales
#Ventana Principal
VB = Tk()
VB.title("Pantalla de Bloqueo")
VB.minsize(500,500)
VB.resizable(width=NO,height=NO)
#Cargar imagenes
def cargarImg(nombre):
    ruta=os.path.join('img',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen
#Canvas Pantalla de Bloqueo
CB = Canvas(VB,width=500,height=500,bg = "#000000")
CB.pack()
#Entry de la clave
Desbloqueo = Entry(CB, width = 30)
Desbloqueo.place(x=155,y=200)
#Boton de Desbloquear
def prent():
    a = str(Desbloqueo.get())
    Desbloquear(a)
PR = Thread(target=prent,args=())
def Desbloquear(key):
    if key == "Desbloquear":
        return VP()
    else:
        PR.start
        lbl1 = Label(CB, text = "La contraseña es incorrecta").place(x=150,y=150)
        return 
BD = Button(CB, text = "Desbloquear" , command = PR.start, bg = "#65BADF", fg = "#000000",width = 10 , height = 1)
BD.place(x=60,y=90)
#Pantalla principal
def VP():
    VB.withdraw()
    VP = Toplevel()
    VP.title("Pantalla Principal")
    VP.minsize(500,500)
    VP.resizable(width=NO,height=NO)
    CP = Canvas(VP,width = 500,heigth=500, bg = "#000000")
    CP.place(x=0,y=0)

VB.mainloop()
