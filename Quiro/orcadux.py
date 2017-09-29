import random
class Ahorcado:
    def __init__ (self):
        self.atte =  3
        self.palabras = ["Perro","Calle","Gato","Guaro","Agua"] 
        self.palabra = random.choice(["Perro","Calle","Gato","Guaro","Agua"])
        self.incog= self.equis(self.palabra.lower())
        self.comp = self.incog
    def intento(self, let):
       
                
        letra = let.lower()
            
        for i in range(0,len(self.palabra)):
              if letra==self.palabra.lower()[i]:
                  self.incog=list(self.incog)
                  self.incog[i]=letra
                  self.incog="".join(self.incog)

        if self.incog==self.comp and self.atte !=1:
              self.atte-=1
              
              print(self.atte)

              return self.otra()
            
        elif self.palabra.lower() == self.incog:
            return self.ganar()
        elif self.atte==1:
            return self.perder()
        self.comp=self.incog
        return self.comp
    
    def equis(self,x):
        ind=len(x)
        x=""
        for i in range(0,ind):
            x+="x"
        return x
    
    def letra(self, letra):
        print(letra)
        return self.intento(letra)

    def ganar(self):
        return "Ganaste!"
    def perder(self):
        return "Perdiste!"
    def otra(self):
        return "Ingrese otra letra!"
