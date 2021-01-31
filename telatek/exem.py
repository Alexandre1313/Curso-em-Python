from tkinter import *


class Aplication:
    def __init__(self):
        self.janela = Tk()
        self.titulo = self.janela.title('MEU APP')
        self.config = self.janela.configure(background='black')
        self.geometria = self.janela.geometry('1000x500')
        self.tamajus = self.janela.resizable(True, True)
        self.min = self.janela.minsize(width=1000, height=500)
        self.frame_1 = Frame(bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.007, rely=0.007, relwidth=0.986, relheight=0.4895)
        self.frame_2 = Frame(bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.007, rely=0.5035, relwidth=0.986, relheight=0.4895)

    def iniciar(self):
        jan = self.janela
        jani = jan


a = Aplication().iniciar()
