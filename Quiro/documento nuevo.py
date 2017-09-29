from tkinter import *
VP = Tk()
VP.title("Pantalla Principal")
VP.minsize(500,500)
VP.resizable(width=NO,height=NO)

CP = Canvas(VP,width=500,height=500,bg="#000000")
CP.pack()

class Calculadora:

    def __init__(self):

        self.result = 0

        self.nums = []

        self.ops = []

    def sumar(self):

        self.ops.append("+")

    def resta(self):

        self.ops.append("-")
        
    def division(self):

        self.ops.append("/")

    def multiplicacion(self):

        self.ops.append("x")

    def igual(self):

        rest = 0
        
        for i in range(0,len(self.ops)):
            
            if self.ops[i - rest] == "x":
                a = self.nums[i - rest]
                s = self.nums[i - rest +1]
                rm = a*s
                self.ops.remove("x")
                self.nums.remove(a)
                self.nums.remove(s)
                self.nums.insert(i,rm)
                rest+=1

                
            elif self.ops[i - rest] == "/":
                a = self.nums[i-rest]
                s = self.nums[i+rest+1]
                rm = a*s
                self.ops.remove("/")
                self.nums.remove(a)
                self.nums.remove(s)
                self.nums.insert(i,rm)
                rest += 1
                    
        numLen = len(self.nums)
        opsLen = len(self.ops)

        cero = True
        op = False
        
        Res = 0 
        ind = 0

        for i in range(0, numLen+opsLen):


            if ind > opsLen -1 and op:

                self.result = Res
                    
                return self.result

            elif cero: 
                Res = self.nums[i]
                cero = False
            
            elif self.ops[ind] == "+":

                op = True
                
                ind+=1
    
                Res += self.nums[i]

            elif self.ops[ind] == "-":

                op = True
                
                ind+=1
    
                Res -= self.nums[i]

            
        Res = self.nums[0]
        self.result =  Res


        return self.result
        
    def addNum0(self):
        self.nums.append(0)        
        return
    def addNum1(self):
        self.nums.append(1)        
        return
    def addNum2(self):
        self.nums.append(2)        
        return
    def addNum3(self):
        self.nums.append(3)        
        return
    def addNum4(self):
        self.nums.append(4)        
        return
    def addNum5(self):
        self.nums.append(5)        
        return
    def addNum6(self):
        self.nums.append(6)        
        return
    def addNum7(self):
        self.nums.append(7)        
        return
    def addNum8(self):
        self.nums.append(8)        
        return
    def addNum9(self):
        self.nums.append(9)        
        return


c = Calculadora()

B1 = Button(CP, text = "1", width = 3, command = c.addNum1)
B1.place(x=100,y=100)

B2 = Button(CP, text = "2", width = 3, command = c.addNum2)
B2.place(x=150,y=100)

B3 = Button(CP, text = "3", width = 3, command = c.addNum3)
B3.place(x=200,y=100)

B4 = Button(CP, text = "4", width = 3, command = c.addNum4)
B4.place(x=100,y=150)

B5 = Button(CP, text = "5", width = 3, command = c.addNum5)
B5.place(x=150,y=150)

B6 = Button(CP, text = "6", width = 3, command = c.addNum6)
B6.place(x=200,y=150)

B7 = Button(CP, text = "7", width = 3, command = c.addNum7)
B7.place(x=100,y=200)

B8 = Button(CP, text = "8", width = 3, command = c.addNum8)
B8.place(x=150,y=200)

B9 = Button(CP, text = "9", width = 3, command = c.addNum9)
B9.place(x=200,y=200)

B0 = Button(CP, text = "0", width = 3, command = c.addNum0)
B0.place(x=100,y=250)

Bs = Button(CP, text = "+", width = 3, command = c.sumar)
Bs.place(x=150,y=250)

Br = Button(CP, text = "-", width = 3, command = c.resta)
Br.place(x=200,y=250)

Bm = Button(CP, text = "x", width = 3, command = c.multiplicacion)
Bm.place(x=100,y=300)

Bd = Button(CP, text = "/", width = 3, command = c.division)
Bd.place(x=150,y=300)

def prent():
    c.igual()
    L = Label(CP,width=10,height=15, text = c.result).place(x=300,y=100)
    c.result = 0
    c.ops = []
    c.nums = []
    
Bi = Button(CP, text = "=", width = 3, command = prent)
Bi.place(x=200,y=300)


