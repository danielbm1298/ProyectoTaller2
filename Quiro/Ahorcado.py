import random
def equis(x):
    ind=len(x)
    x=""
    for i in range(0,ind):
        x+="x"
    return x
        
def ahorcado():
    palabra= random.choice(["Bebida","Agua","Tool","Gato","Perro"])
    vidas = 3

    palabra=palabra.lower()
    incog= equis(palabra)
    comp=incog

    while palabra!=incog:
        letra=input("Ingrese una letra: ")
        letra=letra.lower()
        
        for i in range(0,len(palabra)):
            if letra==palabra[i]:
                incog=list(incog)
                incog[i]=letra
                incog="".join(incog)
        print(incog)

        if incog==comp and vidas !=1:
            vidas-=1
            print("Ingrese otra letra!")
            print(vidas)
        elif vidas==1:
            return("Perdiste! :(")
        comp=incog
    return "Ganaste!"
