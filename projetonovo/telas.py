import PySimpleGUI as Sg
from random import randint
from projetonovo import bancodados


Sg.theme('DarkTeal11')


def janela1():
    layout1 = [
        [Sg.Text('SEJA BEM VINDO!')],
        [Sg.Button('Entrar(^)', size=(11, 0)), Sg.Button('Sair(x)', size=(11, 0))]
    ]
    window = Sg.Window('ALEXX APP', layout1, size=(400, 70), element_justification='center')
    event, value = window.read()
    if event == 'Entrar(^)':
        window.close()
    if event == 'Sair(x)' or event == Sg.WIN_CLOSED:
        exit()


def janela3():
    layout2 = [
        [Sg.Text('Informe o nome do funcionário:'), Sg.InputText('', size=(60, 0), key='-nome-')],
        [Sg.Text('____' * 22)],
        [Sg.Button('Adicionar', size=(10, 0)), Sg.Button('Deletar', size=(10, 0))],
        [Sg.Text('Funcionários cadastrados:')],
        [Sg.Listbox(['Nome'], size=(85, 23), key='-Box-')],
        [Sg.Text('____' * 22)],
        [Sg.Button('Sair(x)', size=(10, 0))]
    ]
    window = Sg.Window('ALEXX APP', layout2, size=(735, 600))
    while True:
        event, value = window.read()
        if event == 'Sair(x)' or event == Sg.WIN_CLOSED:
            exit()
        if event == 'Adicionar':
            cadastro = randint(1, 999)
            nome = value['-nome-'].strip().title()
            if nome != '':
                bancodados.escrever(cadastro, nome)
            window.find_element('-nome-').Update('')


janela1()
janela3()
