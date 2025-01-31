from tkinter import *

class Principal:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial","10")
        #Definindo um Container Pai
        self.Container1 = Frame(master)
        self.Container1["pady"] = 10
        self.Container1["bg"] = "light blue"
        self.Container1.pack()
        #Criando um Container NOME
        self.Container2 = Frame(master)
        self.Container2["padx"] = 20
        self.Container2["bg"] = "light blue"
        self.Container2.pack()
        #Criando um Container SENHA
        self.Container3 = Frame(master)
        self.Container3["padx"] = 20
        self.Container3["bg"] = "light blue"
        self.Container3.pack()
        #Criando um Container para o botão AUTENTICAR e Mensagem
        self.Container4 = Frame (master)
        self.Container4["pady"] = 20
        self.Container4["bg"]="light blue"
        self.Container4.pack()
        #Titulo
        self.titulo = Label(self.Container1, text="Dados do Usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["bg"] = "light blue"
        self.titulo.pack()
        #Input_Nome
        self.nomeLabel = Label(self.Container2, text=" Nome:", font=self.fontePadrao)
        self.nomeLabel["bg"] = "light blue"
        self.nomeLabel.pack(side=LEFT)
        self.nome= Entry(self.Container2)
        self.nome.focus()
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        #Input_Senha
        self.senhaLabel = Label(self.Container3, text=" Senha:", font=self.fontePadrao)
        self.senhaLabel["bg"] = "light blue"
        self.senhaLabel.pack(side=LEFT)
        self.senha= Entry(self.Container3)
        self.senha["width"] = 30
        self.senha["font"]= self.fontePadrao
        self.senha["show"]= "*"
        self.senha.pack(side=LEFT)
        #Autenticação e Mensagem
        self.autenticar = Button(self.Container4)
        self.autenticar["text"] = "AUTENTICAR"
        self.autenticar["font"] = ("Calibri", "10", "bold")
        self.autenticar["width"] = 12
        self.autenticar["bg"] = "white"
        self.autenticar["command"] = self.verificarSenha
        self.autenticar.pack()
        self.mensagem = Label(self.Container4, text="", font=self.fontePadrao)
        self.mensagem["bg"] = "light blue"
        self.mensagem.pack()
        #Sair
        self.sair = Button()
        self.sair["text"] = "SAIR"
        self.sair["font"] = ("Calibri", "10", "bold")
        self.sair["width"] = 5
        self.sair["command"] = quit
        self.sair.pack(side=TOP)

#Método para verificar a SENHA
    def verificarSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "LucasCruz" and senha == "1515":
            self.mensagem["text"] = "Autenticado!"
            self.nome["fg"] = "gray"
            self.senha["fg"] = "gray"
            self.sair.focus_focus()
        else:
            self.mensagem["text"] = "Usuário e/ou senha incorretos!"
            self.senha.delete(0,END)
            self.nome.delete(0,END)
            self.nome.focus()


tela= Tk()
tela.title ("TELA DE LOGIN")
tela ["bg"] = "light blue"
tela.geometry ("400x250")

Principal(tela)
tela.mainloop()