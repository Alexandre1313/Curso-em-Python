from tkinter.filedialog import askopenfilenames
from pygame import mixer
from tkinter import *

music = list()
item = 0
tam = len(music)


class Reprodutor:
    def __init__(self):
        pass

    @staticmethod
    def escolher():
        selecionar = askopenfilenames(initialdir='g:/musicas/',
                                      filetypes=(('Arquivos de audio', '*.mp3'), ('All Files', '*.*')),
                                      title='Selecione as músicas')
        for c in selecionar:
            print(f'\033[36m{c}\033[m'.upper())
            if c not in music:
                music.append(c)
        print()
        return music

    @staticmethod
    def reproduzir():
        import pygame
        pygame.init()
        mixer.init()
        for c, item in enumerate(music):
            while c <= tam:
                musica = mixer.music.load(item)
                musica = mixer.music.play()
                pygame.event.wait()
                pass

    @staticmethod
    def parar():
        musica = mixer.music.stop()

    @staticmethod
    def pausar():
        musica = mixer.music.pause()

    @staticmethod
    def retomar():
        musica = mixer.music.unpause()


def anterior():
    global item
    if item - 1 == -1:  # Se for -1 ele volta não decrementa, ficando em 0.
        pass
    else:
        item -= 1
    # print(item)
    musica = mixer.music.load(music[item])
    musica = mixer.music.play()


def proxima():
    global item  # Usando uma variável de fora
    item += 1
    # print(item) # Utilizei para checar o que havia de errado.
    try:
        musica = mixer.music.load(music[item])
        musica = mixer.music.play()
    except IndexError:  # Se o Index nao existir, isso vai impedir que o valor de item incremente.
        item -= 1


player = Reprodutor
janela = Tk()
janela.title("ALEXX MUSIC PLAYER")

# Esta parte é que está com problemas
bt_escolher = Button(janela, width=20, text="CARREGAR MÚSICAS", command=player.escolher)
bt_proxima = Button(janela, width=10, text="PRÓXIMA", command=proxima)
bt_anterior = Button(janela, width=10, text="ANTERIOR", command=anterior)
bt_escolher.place(x=10, y=50)
bt_proxima.place(x=170, y=50)
bt_anterior.place(x=270, y=50)
bt_play = Button(janela, width=10, text="PLAY", command=player.reproduzir)
bt_pause = Button(janela, width=10, text="PAUSAR", command=player.pausar)
bt_stop = Button(janela, width=10, text="PARAR", command=player.parar)
bt_return = Button(janela, width=10, text="RETOMAR", command=player.retomar)
bt_play.place(x=10, y=0)
bt_pause.place(x=110, y=0)
bt_stop.place(x=210, y=0)
bt_return.place(x=310, y=0)
janela.geometry("410x80+450+350")
janela.mainloop()
