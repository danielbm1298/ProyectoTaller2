from tkinter import *
VP = Tk()
VP.title("PP")
VP.minsize(500,500)
VP.resizable(width=NO,height=NO)

CP = Canvas(VP,width=500,height=500,bg="#000000")
CP.pack()

Nombre = Entry(CP, width = 30)
Nombre.place(x=100,y=100)

Telefono = Entry(CP, width = 30)
Telefono.place(x=100, y=150)

Celular = Entry(CP,width=30)
Celular.place(x=100,y=200)

Correo = Entry(CP,width=30)
Correo.place(x=100,y=250)

Foto = Entry(CP,width=30)
Foto.place(x=100,y=300)

def leer():
    with open("contactos.txt","r") as file:
        data = file.read()
        print(data)

def EscribirUsuario():
    with open("contactos.txt","a") as file:
        file.write("\n" + str(Nombre.get()) + "   " )
        Nombre.place(x=1000,y=1000)
        BN.place(x=1000,y=1000)

def EscribirTelefono():
    with open("contactos.txt","a") as file:
        file.write(str(Telefono.get()) + "   " )
        Telefono.place(x=1000,y=1000)
        BT.place(x=1000,y=1000)

def EscribirCelular():
    with open("contactos.txt","a") as file:
        file.write(str(Celular.get()) + "   " )
        Celular.place(x=1000,y=1000)
        BCE.place(x=1000,y=1000)
        
def EscribirCorreo():
    with open("contactos.txt","a") as file:
        file.write(str(Correo.get()) + "   " )
        Correo.place(x=1000,y=1000)
        BCO.place(x=1000,y=1000)
        
def EscribirFoto():
    with open("contactos.txt","a") as file:
        file.write(str(Foto.get()) + "   " )
        Foto.place(x=1000,y=1000)
        BF.place(x=1000,y=1000)
        
BN = Button(CP, text = "Ingresar" , width = 10 , command = EscribirUsuario)
BN.place(x= 300, y=100)

BT = Button(CP, text = "Ingresar", width = 10, command = EscribirTelefono)
BT.place(x=300, y= 150)

BCE = Button(CP, text = "Ingresar", width = 10, command = EscribirCelular)
BCE.place(x=300,y=200)

BCO = Button(CP, text = "Ingresar", width = 10, command = EscribirCorreo)
BCO.place(x=300,y=250)

BF = Button(CP, text = "Ingresar", width = 10, command = EscribirFoto)
BF.place(x=300,y=300)

mainloop()
