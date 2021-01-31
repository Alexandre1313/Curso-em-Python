from tkinter.filedialog import askopenfilenames
import pygame
from random import randint


class Reprod:
    pygame.display.init()
    pygame.mixer.init()

    def __init__(self):
        self.__play_list = list()  # Lista contento o nome das faixas à serem reproduzidas
        self.__lenplay = None  # Usado para definir o len da playlyst
        self.__seletor = 0  # Usado para definir a posição na lista
        self.__volume = 0.2  # Variável de instância para regular o volume do áudio
        self.__volumen = f'{20}%'  # Variável de instância para armazenar o volume de amostra
        self.__musiccam = None  # Variável de instância para armazenar o caminho do áudio à ser carregado
        self.__musicam = 'Hello!'  # Variável de instância para armazenar o que aparecerá no display de texto
        self.__repeat = None  # Variável para repetição de faixa
        self.__loop = None  # Variável que ira setar os loops de play
        self.__random = None
        self.__buton = 'orange'
        self.__buton1 = 'black'

    def stop(self, arg0, arg1, arg2):
        if self.__musiccam is not None:
            pygame.mixer.music.stop()
            Reprod.up1(arg0, arg1, '', arg2, 'Stop!')
            Reprod.set_musicam(self, 'Stop!')

    def pause(self, arg0, arg1):
        if self.__musiccam is not None:
            pygame.mixer.music.pause()
            Reprod.set_musicam(self, 'Paused!')
            Reprod.up1(arg0, arg1, 'Paused!')

    def randomizar(self):
        ram = randint(0, self.__lenplay)
        return ram

    def colours_01(self, arg, arg0):
        nan = randint(0, 19)
        tupla = ('#FFFF00', '#00FF00', '#FF7256', '#00BFFF', '#E0FFFF',
                 '#98FB98', '#8470FF', '#FF69B4', '#9AFF9A', '#FF83FA',
                 '#698B69', '#68228B', '#FF0000', '#00FFFF', '#BCEE68',
                 '#8B7B8B', '#CDB5CD', '#4F4F4F', '#FFFACD', '#CD7054')
        arg.find_element(arg0).Update(background_color=tupla[nan])
        nan = randint(0, 19)
        Reprod.set_buton(self, tupla[nan])
        nan = randint(0, 19)
        Reprod.set_buton1(self, tupla[nan])

    def contin(self, arg0, arg1):
        if self.__musiccam is not None:
            pygame.mixer.music.unpause()
            Reprod.ms(self)
            Reprod.up1(arg0, arg1, 'Tocando>')

    def play(self, arg0, arg1, arg2):
        if Reprod.get_random(self) is True:
            if len(self.__play_list) != 0:
                if self.__musiccam is not None:
                    Reprod.set_loop(self)
                    self.__musiccam = self.__play_list[Reprod.randomizar(self)]
                    pygame.mixer.music.load(self.__musiccam)
                    pygame.mixer.music.play(loops=Reprod.get_loop(self))
                    Reprod.ms(self)
                    Reprod.up1(arg0, arg1, Reprod.get_seletor(self) + 1, arg2, 'Tocando>')
            else:
                Reprod.carregar(self)
        else:
            if len(self.__play_list) != 0:
                if self.__musiccam is not None:
                    Reprod.set_loop(self)
                    pygame.mixer.music.load(self.__musiccam)
                    pygame.mixer.music.play(loops=Reprod.get_loop(self))
                    Reprod.ms(self)
                    Reprod.up1(arg0, arg1, Reprod.get_seletor(self) + 1, arg2, 'Tocando>')
            else:
                Reprod.carregar(self)

    def carregar(self):
        selecionar = askopenfilenames(filetypes=(('Arquivos de audio', '*.mp3'),
                                                 ('Arquivos de audio', '*.flac'), ('All Files', '*.*')),
                                      title='Selecione as faixas')
        for mus in selecionar:
            if mus not in self.__play_list:
                if '.mp3' in mus or '.flac' in mus:
                    self.__play_list.append(mus)
        if len(self.__play_list) > 0:
            Reprod.set_lenplay(self)
        if self.__lenplay is not None:
            self.__musiccam = self.__play_list[self.__seletor]

    def avancar(self, arg0, arg1, arg2):
        if self.__musiccam is not None:
            if self.__seletor < self.__lenplay:
                self.__seletor += 1
                self.__musiccam = self.__play_list[self.__seletor]
                Reprod.play(self, arg0, arg1, arg2)
                Reprod.ms(self)

    def retros(self, arg0, arg1, arg2):
        if self.__musiccam is not None:
            if self.__seletor > 0:
                self.__seletor -= 1
                self.__musiccam = self.__play_list[self.__seletor]
                Reprod.play(self, arg0, arg1, arg2)
                Reprod.ms(self)

    def ms(self):
        m = Reprod.get_musiccam(self)
        m2 = list()
        for c in range((len(m) - 1), - 1, - 1):
            if m[c] == '/':
                break
            else:
                m2.append(m[c])
        nov = ''.join(m2)
        m = nov
        m2 = list()
        for c in range((len(m) - 1), 3, -1):
            m2.append(m[c])
        nov1 = ''.join(m2)
        Reprod.set_musicam(self, nov1)

    def clear_playlist(self, arg0, arg1, arg2):
        self.__play_list.clear()
        Reprod.set_seletor(self, 0)
        Reprod.set_lenplay(self)
        Reprod.set_musicam(self, 'Hello!')
        Reprod.set_musiccam(self, None)
        Reprod.set_repeat(self, None)
        Reprod.up1(arg0, arg1, '', arg2, '')
        pygame.mixer.music.unload()

    @staticmethod
    def _should_round_down(val: float):
        if val < 0:
            return ((val * -1) % 1) < 0.5
        return (val % 1) < 0.5

    @staticmethod
    def _round(val: float, ndigits=0):
        import math
        if ndigits > 0:
            val *= 10 ** (ndigits - 1)
        is_positive = val > 0
        tmp_val = val
        if not is_positive:
            tmp_val *= -1
        rounded_value = math.floor(tmp_val) if Reprod._should_round_down(val) else math.ceil(tmp_val)
        if not is_positive:
            rounded_value *= -1
        if ndigits > 0:
            rounded_value /= 10 ** (ndigits - 1)
        return rounded_value

    def up1(*lst):
        arg = lst[0]
        for i in range(0, (len(lst) - 1), 1):
            if i == 1 or i == 3:
                arg.find_element(lst[i]).Update(lst[i + 1])
            if i > 4 and i % 2 != 0:
                if lst[i + 1] != -1.0 and lst[i + 1] != -2.0 and lst[i + 1] != 'lz':
                    arg.find_element(lst[i]).Update(lst[i + 1])
                else:
                    if lst[i + 1] == -1.0:
                        arg.find_element(lst[i]).Update('"?"')
                    if lst[i + 1] == -2.0:
                        arg.find_element(lst[i]).Update('')
                    if lst[i + 1] == 'lz':
                        if 'T' in lst:
                            arg.find_element(lst[i]).Update('')
                        else:
                            if lst[i] == '-prv3-':
                                arg.find_element(lst[i]).Update('Prova 03 >>')
                            if lst[i] == '-prv4-':
                                arg.find_element(lst[i]).Update('Prova 04 >>')
                            if lst[i] == '-mgl3-':
                                arg.find_element(lst[i]).Update('Média prova 03 >>')
                            if lst[i] == '-mgl4-':
                                arg.find_element(lst[i]).Update('Média prova 04 >>')

    def set_seletor(self, arg):
        self.__seletor = arg

    def set_random(self, arg):
        self.__random = arg

    def set_buton(self, arg):
        self.__buton = arg

    def set_buton1(self, arg):
        self.__buton1 = arg

    def set_volume(self, arg, vol):
        Reprod._should_round_down(arg)
        d = Reprod._round(arg, 2)
        self.__volume = d
        self.__volumen = f'{vol}%'

    def set_lenplay(self):
        self.__lenplay = len(self.__play_list) - 1

    def set_musicam(self, arg):
        self.__musicam = arg

    def set_musiccam(self, arg):
        self.__musiccam = arg

    def set_repeat(self, arg):
        self.__repeat = arg

    def set_loop(self):
        if Reprod.get_repeat(self) is True:
            self.__loop = -1
        else:
            self.__loop = 0

    def get_volume(self):
        return self.__volume

    def get_voluman(self):
        return self.__volumen

    def get_seletor(self):
        return self.__seletor

    def get_random(self):
        return self.__random

    def get_musiccam(self):
        return self.__musiccam

    def get_musicam(self):
        return self.__musicam

    def get_play_list(self):
        return self.__play_list

    def get_lenplay(self):
        return self.__lenplay

    def get_repeat(self):
        return self.__repeat

    def get_loop(self):
        return self.__loop

    def get_buton(self):
        return self.__buton

    def get_buton1(self):
        return self.__buton1
