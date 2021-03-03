import PySimpleGUI as Sg
import pygame
from Reprodutor_novo import functions


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


def linha22(arg):
    linhas = Sg.Text('____' * arg)
    return linhas


def reprodutor():
    x = functions.Reprod()
    Sg.theme('Black')
    Sg.SetOptions(button_color=(x.get_buton(), x.get_buton1()))
    display = x.get_musicam()
    volume1 = x.get_voluman()
    nfaixas = '0'
    layout = [
        [Sg.Text('MY MUSIC PLAYER', size=(30, 1), justification='center', font=("Helvetica", 25),
                 relief=Sg.RELIEF_SUNKEN, border_width=5, background_color='#D8BFD8',
                 key='-rt-', text_color='#000000')],
        [Sg.Button('PLAY>>', size=(11, 0), border_width=1), Sg.Button('PAUSE', size=(11, 0), border_width=1),
         Sg.Button('NEXT>', size=(11, 0), border_width=1), Sg.Button('FALL BACK<', size=(11, 0), border_width=1),
         Sg.Button('CONTINUE', size=(11, 0), border_width=1), Sg.Button('STOP', size=(11, 0), border_width=1)],
        [Sg.Text('', size=(9, 0), border_width=2, text_color='#00FFFF', justification='left',
                 font=('arial', 10), key='-st-', relief=Sg.RELIEF_SUNKEN),
         Sg.Text('', size=(3, 0), border_width=2, text_color='#FF8247', justification='center',
                 font=('arial', 14), key='-fx-', relief='sunken')],
        [Sg.Text('')],
        [Sg.Text(display, size=(48, 3), key='-even-', background_color='#000000', border_width=7,
                 text_color='#ADFF2F', relief='flat', justification='center', font=('arial', 16))],
        [Sg.Button('Select', size=(7, 0)),
         Sg.Button('Exit', size=(7, 0)),
         Sg.Button('vol +', size=(4, 0)),
         Sg.Text(volume1, size=(5, 0), border_width=2, text_color='#00FFFF',
                 relief='sunken', key='-vol-', justification='center'),
         Sg.Button('vol -', size=(4, 0)),
         Sg.Checkbox('Repeat', default=False, key='-av-'),
         Sg.Checkbox('Random', default=False, key='-ry-'),
         Sg.Text('Tracks'),
         Sg.Text(nfaixas, size=(4, 0), key='-nf-', border_width=2, text_color='#00FF7F',
                 relief='sunken', justification='center'),
         Sg.Button('Clear', size=(7, 0))]
    ]
    reprod = Sg.FlexForm('MUSIC PLAYER', use_default_focus=False, no_titlebar=False,
                         titlebar_background_color='#000000').Layout(layout)
    volum = 0.2
    volumam = 20
    while True:
        event, value = reprod.read()
        if event == 'Exit' or event == Sg.WIN_CLOSED:
            x.stop(reprod, '-fx-', '-st-')
            break
        if event == 'vol +' or event == 'vol -':
            if event == 'vol +':
                if x.get_volume() < 1.0:
                    volum += 0.1
                    volumam += 10
            if event == 'vol -':
                if x.get_volume() > 0.0:
                    volum -= 0.1
                    volumam -= 10
            x.set_volume(volum, volumam)
        if event == 'Select':
            x.carregar()
        if event == 'NEXT>':
            x.avancar(reprod, '-fx-', '-st-')
        if event == 'FALL BACK<':
            x.retros(reprod, '-fx-', '-st-')
        if event == 'PLAY>>':
            x.play(reprod, '-fx-', '-st-')
        if event == 'STOP':
            x.stop(reprod, '-fx-', '-st-')
        if event == 'Clear':
            x.clear_playlist(reprod, '-fx-', '-st-')
        if event == 'PAUSE':
            x.pause(reprod, '-st-')
        if event == 'CONTINUE':
            x.contin(reprod, '-st-')
        x.set_random(value['-ry-'])
        x.set_repeat(value['-av-'])
        pygame.mixer.music.set_volume(x.get_volume())
        up1(reprod, '-vol-', x.get_voluman())
        up1(reprod, '-even-', x.get_musicam())
        if x.get_lenplay() is not None:
            up1(reprod, '-nf-', x.get_lenplay() + 1)
        x.colours_01(reprod, '-rt-')
        Sg.SetOptions(x.get_buton(), x.get_buton1())
    reprod.close()
