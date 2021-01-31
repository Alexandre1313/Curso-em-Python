import PySimpleGUI as Sg
from horas import functions


def janela_inserir():
    Sg.theme('DarkAmber')
    layout0 = [
        [Sg.Text('Hora entrada manhã >>', size=(18, 0), background_color='#424242'),
         Sg.InputText('', size=(3, 0), background_color='#424242', text_color='#088A4B',
                      border_width=2, key='-h1-'),
         Sg.InputText('', size=(3, 0), background_color='#424242', text_color='#088A4B',
                      border_width=2, key='-m1-'),
         Sg.Text('Hora entrada tarde >>', size=(18, 0), background_color='#424242'),
         Sg.InputText('', size=(3, 0), background_color='#424242', text_color='#088A4B',
                      border_width=2, key='-h2-'),
         Sg.InputText('', size=(3, 0), background_color='#424242', text_color='#088A4B',
                      border_width=2, key='-m2-')],
        [Sg.Text('Hora saída almoço >>', size=(18, 0), background_color='#424242'),
         Sg.InputText('', size=(3, 0), background_color='#424242', text_color='#088A4B',
                      border_width=2, key='-h3-'),
         Sg.InputText('', size=(3, 0), background_color='#424242', text_color='#088A4B',
                      border_width=2, key='-m3-'),
         Sg.Text('Hora saída final >>', size=(18, 0), background_color='#424242'),
         Sg.InputText('', size=(3, 0), background_color='#424242', text_color='#088A4B',
                      border_width=2, key='-h4-'),
         Sg.InputText('', size=(3, 0), background_color='#424242', text_color='#088A4B',
                      border_width=2, key='-m4-')],
        [Sg.Output(size=(70, 10), text_color='#64FE2E', background_color='#000000')],
        [Sg.Button('Salvar', size=(10, 0), tooltip='  Salvar dados!  ',
                   border_width=4), Sg.Button('Sair ', size=(10, 0), tooltip='  Sair do sistema!  ',
                                              border_width=4),
         Sg.Checkbox('Formato 12 horas', default=True, tooltip='  Desmarque para formato 12 horas  ')],
    ]
    inserir = Sg.FlexForm('CADASTRO').layout(layout0)
    while True:
        event, values = inserir.read()
        if event == 'Sair ' or event == Sg.WIN_CLOSED:
            break
        if event == 'Salvar':
            h1 = values['-h1-']
            m1 = values['-m1-']
            h2 = values['-h2-']
            m2 = values['-m2-']
            h3 = values['-h3-']
            m3 = values['-m3-']
            h4 = values['-h4-']
            m4 = values['-m4-']
            jk = functions.convert(h1, m1, h2, m2, h3, m3, h4, m4)
            print(jk)
    inserir.close()


janela_inserir()
