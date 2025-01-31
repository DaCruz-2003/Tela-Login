from tkinter import *

class Principal:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial","10")
        self.Container1 = Frame(master)


tela= Tk()
tela.title ("TELA DE LOGIN")
tela ["bg"] = "light blue"
tela.geometry ("400x250")

Principal(tela)
tela.mainloop()