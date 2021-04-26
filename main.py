from tkinter import *


class Calculadora:
    def __init__(self, master=None):
        self.fonte = ("Arial", "11")
        # container1 irá conter o título
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["pady"] = 5
        self.container5.pack()

        self.titulo = Label(self.container1, text="Calculadora")
        self.titulo["font"] = ("Arial", "11", "bold")
        self.titulo.pack()

        self.n1Label = Label(self.container2, text="N1", font=self.fonte)
        self.n1Label.pack(side=LEFT)

        self.n1 = Entry(self.container2)
        self.n1["width"] = 10
        self.n1["font"] = self.fonte
        self.n1.pack(side=RIGHT)

        self.n2Label = Label(self.container3, text="N2", font=self.fonte)
        self.n2Label.pack(side=LEFT)

        self.n2 = Entry(self.container3)
        self.n2["width"] = 10
        self.n2["font"] = self.fonte
        self.n2.pack(side=RIGHT)

        # fonte para os botões
        self.fonteB = ("Calibri", "15")
        self.somar = Button(self.container4)
        self.somar["text"] = "+"
        self.somar["font"] = self.fonteB
        self.somar["width"] = 5
        self.somar["command"] = self.soma
        self.somar.pack(side=LEFT)

        self.subtrair = Button(self.container4)
        self.subtrair["text"] = "-"
        self.subtrair["font"] = self.fonteB
        self.subtrair["width"] = 5
        self.subtrair["command"] = self.subtrai
        self.subtrair.pack(side=LEFT)

        self.multiplicar = Button(self.container4)
        self.multiplicar["text"] = "*"
        self.multiplicar["font"] = self.fonteB
        self.multiplicar["width"] = 5
        self.multiplicar["command"] = self.multiplica
        self.multiplicar.pack(side=LEFT)

        self.dividir = Button(self.container4)
        self.dividir["text"] = "/"
        self.dividir["font"] = self.fonteB
        self.dividir["width"] = 2
        self.dividir["command"] = self.divisao
        self.dividir.pack()

        self.mensagem = Label(self.container5, text="", font=self.fonte)
        self.mensagem.pack()

    def soma(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        try:
            n1 = float(n1)
            n2 = float(n2)
            self.mensagem["text"] = "{} + {} = {}".format(n1, n2, n1 + n2)
        except:
            self.mensagem["text"] = "Ocorreu um erro, as entradas devem ser numericas"

    def subtrai(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        try:
            n1 = float(n1)
            n2 = float(n2)
            self.mensagem["text"] = "{} - {} = {}".format(n1, n2, n1 - n2)
        except:
            self.mensagem["text"] = "Ocorreu um erro, as entradas devem ser numericas"

    def multiplica(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        try:
            n1 = float(n1)
            n2 = float(n2)
            self.mensagem["text"] = "{} * {} = {}".format(n1, n2, n1 * n2)
        except:
            self.mensagem["text"] = "Ocorreu um erro, as entradas devem ser numericas"

    def divisao(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        try:

            n1 = float(n1)
            n2 = float(n2)
            if n1 != 0:
                div = n1 / n2
                self.mensagem["text"] = "{} / {} = {}".format(n1, n2, div)
                return True
            else:
                self.mensagem["text"] = "Divisão impossível"
        except:
            self.mensagem["text"] = "Ocorreu um erro, as entradas devem ser numericas"
            return False


root = Tk()
Calculadora(root)
root.mainloop()
