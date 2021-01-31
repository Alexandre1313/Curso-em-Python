import PySimpleGUI as Sg
import pygame
from tocador import classes


def _should_round_down(val: float):
    if val < 0:
        return ((val * -1) % 1) < 0.5
    return (val % 1) < 0.5


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


def _round(val: float, ndigits=0):
    import math
    if ndigits > 0:
        val *= 10 ** (ndigits - 1)
    is_positive = val > 0
    tmp_val = val
    if not is_positive:
        tmp_val *= -1
    rounded_value = math.floor(tmp_val) if _should_round_down(val) else math.ceil(tmp_val)
    if not is_positive:
        rounded_value *= -1
    if ndigits > 0:
        rounded_value /= 10 ** (ndigits - 1)
    return rounded_value


def linha22(arg):
    linhas = Sg.Text('____' * arg)
    return linhas


def reprodutor():
    Sg.theme('DarkBlack')
    layout = [
        [Sg.Text('MY MUSIC PLAYER', size=(31, 1), justification='center', font=("Helvetica", 25),
                 relief=Sg.RELIEF_RAISED, background_color='#00FF7F', text_color='#000000')],
        [Sg.Button('PLAY>>', size=(11, 0), border_width=1), Sg.Button('PAUSE', size=(11, 0), border_width=1),
         Sg.Button('NEXT>', size=(11, 0), border_width=1), Sg.Button('FALL BACK<', size=(11, 0), border_width=1),
         Sg.Button('CONTINUE', size=(11, 0), border_width=1), Sg.Button('STOP', size=(11, 0), border_width=1)],
        [Sg.Text('')],
        [Sg.Text('', size=(50, 3), key='-even-',
                 text_color='#ADFF2F', relief='flat', justification='center', font=('arial', 16))],
        [Sg.Button('Select', size=(11, 0)),
         Sg.Button('Exit', size=(11, 0)),
         Sg.Button('vol +', size=(5, 0)),
         Sg.Text('', size=(2, 0), border_width=0, text_color='#00FFFF', key='-vol-', justification='center'),
         Sg.Button('vol -', size=(5, 0)),
         Sg.Checkbox('Repeat', default=True, key='-av-')]
    ]
    reprod = Sg.FlexForm('MUSIC PLAYER').Layout(layout)
    x = classes.Tocador()
    volum = 0.3
    volumam = 3
    while True:
        event, value = reprod.read()
        if event == 'Exit' or event == Sg.WIN_CLOSED:
            x.stop()
            break
        if event == 'Select':
            x.carregar()
        if event == 'PLAY>>':
            x.rep(value['-av-'])
            x.play()
            up1(reprod, '-even-', x.gat_music())
        if event == 'vol +':
            if volum < 0.9:
                volum += 0.1
                volumam += 1
        if event == 'vol -':
            if volum > 0.1:
                volum -= 0.1
                volumam -= 1
        if event == 'STOP':
            x.stop()
            up1(reprod, '-even-', x.gat_music())
        if event == 'PAUSE':
            x.pause()
            up1(reprod, '-even-', x.gat_music())
        if event == 'CONTINUE':
            x.cont()
            up1(reprod, '-even-', x.gat_music())

        pygame.mixer.music.set_volume(volum)
        up1(reprod, '-vol-', volumam)
    reprod.close()
