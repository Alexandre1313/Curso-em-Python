from tkinter import *

janela = Tk()


class Aplication:
    def __init__(self):
        self.janela = janela
        self.frame_1 = Frame
        self.frame_2 = Frame
        self.tela()
        self.frames_da_tela()
        self.botoes()
        janela.mainloop()

    @staticmethod
    def tela():
        janela.title('MEU APP')
        janela.configure(background='black')
        janela.geometry('1000x500')
        janela.resizable(True, True)
        janela.minsize(width=1000, height=500)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.007, rely=0.007, relwidth=0.986, relheight=0.4895)
        self.frame_2 = Frame(self.janela, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.007, rely=0.5035, relwidth=0.986, relheight=0.4895)

    def botoes(self):
        bt_limpar = Button(self.frame_1)


Aplication()
