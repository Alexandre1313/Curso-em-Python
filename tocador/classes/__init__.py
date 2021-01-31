from tkinter.filedialog import askopenfilenames
import pygame


class Tocador:
    pygame.display.init()
    pygame.mixer.init()

    def __init__(self):
        self.__play_list = list()
        self.__selector = 0
        self.__verd = False
        self.__nmusic1 = 'Playlist vazia! Carregue faixas para reproduzir!.mp3'
        self.__nmusic = self.__nmusic1
        self.__repeat1 = None

    def rep(self, arg):
        if arg is True:
            av = -1
        else:
            av = 0
        self.__repeat1 = av

    @staticmethod
    def ms(arg):
        m = arg
        m2 = list()
        for c in range((len(m) - 1), - 1, - 1):
            if m[c] == '/':
                break
            else:
                m2.append(m[c])
        nov = ''.join(m2)
        return nov

    @staticmethod
    def ms1(arg):
        m = arg
        m2 = list()
        for c in range((len(m) - 1), 3, -1):
            m2.append(m[c])
        nov1 = ''.join(m2)
        return nov1

    def carregar(self):
        selecionar = askopenfilenames(filetypes=(('Arquivos de audio', '*.mp3'), ('All Files', '*.*')),
                                      title='Selecione as faixas')
        for mus in selecionar:
            if mus not in self.__play_list:
                self.__play_list.append(mus)

    def play(self):
        if self.__play_list:
            if self.__selector < len(self.__play_list) - 1:
                self.__selector += 1
            else:
                self.__selector = 0
            pygame.mixer.music.load(self.__play_list[self.__selector])
            pygame.mixer.music.play(start=0.0, loops=self.__repeat1)
            n = Tocador.ms(self.__play_list[self.__selector])
            n1 = Tocador.ms1(n)
            self.__nmusic = n1
        else:
            n = Tocador.ms(self.__nmusic1)
            n1 = Tocador.ms1(n)
            self.__nmusic = n1

    def stop(self):
        self.__nmusic = 'Stop!'
        Tocador.setverd(self, True)
        pygame.mixer.music.stop()

    def pause(self):
        self.__nmusic = 'Paused!'
        pygame.mixer.music.pause()

    def cont(self):
        if self.__play_list:
            n = Tocador.ms(self.__play_list[self.__selector])
            n1 = Tocador.ms1(n)
            self.__nmusic = n1
            pygame.mixer.music.unpause()
        else:
            n = Tocador.ms(self.__nmusic1)
            n1 = Tocador.ms1(n)
            self.__nmusic = n1
            pygame.mixer.music.unpause()

    def gat_music(self):
        return self.__nmusic

    def setverd(self, arg):
        self.__verd = arg
