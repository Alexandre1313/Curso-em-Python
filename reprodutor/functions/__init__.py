from tkinter.filedialog import askopenfilenames
from pygame import mixer


def esc():
    musicas = []
    selecionar = askopenfilenames(filetypes=(('Arquivos de audio', '*.mp3'), ('All Files', '*.*')),
                                  title='Selecione as músicas')
    for itens in selecionar:
        musicas.append(itens)
    return musicas


class Repod:
    def __init__(self, lista=None, num=0):
        if lista:
            self.lis = lista
            self.at = ''
            self.ind = num
            self.cont = 0
            self.dep = 2
            self.mut = ''
        else:
            self.lis = []
            self.at = ''
            self.ind = num
            self.cont = 0
            self.dep = 2
            self.mut = ''

    def retor(self):
        val = self.cont
        return val

    def play(self):
        if self.lis:
            mixer.init()
            try:
                for c in range(0, len(self.lis), 1):
                    if self.lis:
                        self.at = self.lis[self.ind]
                        mixer.music.load(self.at)
                        mixer.music.play()
                        print(f'TOCANDO >>> {self.at}')
                        mixer.music.queue(self.lis[self.ind + 1])
                        if self.ind < len(self.lis) - 1:
                            self.ind += 1
                        else:
                            self.ind = 0
            except Exception as erro:
                print(erro)
            else:
                pass

    def pause(self):
        if self.lis:
            try:
                mixer.music.pause()
            except Exception as erro:
                print(erro)
            else:
                print(f'PAUSE')
        else:
            print(f'Playlist vazia, selecione faixas!')

    def retom(self):
        if self.lis:
            try:
                mixer.music.unpause()
            except Exception as erro:
                print(erro)
            else:
                print(f'CONTINUANDO... >>> {self.at}')
        else:
            print(f'Playlist vazia, selecione faixas!')

    def parar(self):
        if self.lis:
            try:
                mixer.music.stop()
            except Exception as erro:
                print(erro)
            else:
                print(f'FINALIZADO!')
        else:
            print(f'Playlist vazia, selecione faixas!')

    def prox(self):
        if self.lis:
            try:
                n = self.ind
                self.at = self.lis[n]
                Repod.play(self)
                self.cont += 1
            except Exception as erro:
                print(erro)
            else:
                print(f'TOCANDO >>> {self.at}')
        else:
            print(f'Playlist vazia, selecione faixas!')



