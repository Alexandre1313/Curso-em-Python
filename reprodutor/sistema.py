import PySimpleGUI as Sg
from reprodutor import functions


def linha22(arg):
    linhas = Sg.Text('____' * arg)
    return linhas


def atual(lst1, lst2):
    ghj = lst1
    for v in ghj:
        lst2.append(v)


def reprodutor():
    fff = []
    Sg.theme('LightGreen9')
    layout = [
        [Sg.Text('MY MUSIC PLAYER', size=(30, 1), justification='center', font=("Helvetica", 25),
                 relief=Sg.RELIEF_RAISED, background_color='#00FF7F', text_color='#000000')],
        [Sg.Button('PLAY>>', size=(11, 0), border_width=5), Sg.Button('PAUSE', size=(11, 0), border_width=5),
         Sg.Button('NEXT>', size=(11, 0), border_width=5), Sg.Button('FALL BACK<', size=(11, 0), border_width=5)],
        [Sg.Button('CONTINUE', size=(11, 0), border_width=5), Sg.Button('STOP', size=(11, 0), border_width=5)],
        [Sg.Combo(fff, size=(60, 0), key='-comb-')],
        [linha22(21)],
        [Sg.Output(size=(79, 10), key='-out-', text_color='#00FF7F', background_color='#00000f')],
        [linha22(21)],
        [Sg.Button('Select', size=(11, 0)),
         Sg.Button('Exit', size=(11, 0))]
    ]
    reprod = Sg.FlexForm('MUSIC PLAYER').Layout(layout)
    musica = []
    num = 0
    while True:
        a = functions.Repod(musica, num)
        event, value = reprod.read()
        if event == 'Exit' or event == Sg.WIN_CLOSED:
            break
        if event == 'Select':
            music0 = functions.esc()
            for m in music0:
                if m not in musica:
                    musica.append(m)
                    print('Música adicionada à playlist!')
                    print(m)
                else:
                    print('Música ja se encontra na playlist!')
        if event == 'PLAY>>':
            if musica:
                a.play()
            else:
                print(f'Playlist vazia, selecione faixas!')

        if event == 'PAUSE':
            a.pause()
        if event == 'CONTINUE':
            a.retom()
        if event == 'STOP':
            a.parar()
        if event == 'NEXT>':
            if num < len(musica) - 1:
                num += 1
            else:
                num = 0
            a.prox()
    reprod.close()


reprodutor()
