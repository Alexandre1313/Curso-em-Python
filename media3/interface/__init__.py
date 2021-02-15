import PySimpleGUI as Sg
import media3.funtions


def linha22(arg):
    linhas = Sg.Text('=' * arg)
    return linhas


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


def up(*lst):
    arg = lst[0]
    for i in range((len(lst) - 1), 0, -1):
        arg.find_element(lst[i]).Update('')


def pop_confirm(arg):
    Sg.theme('DarkGreen6')
    layout3 = [
        [Sg.Text('Deseja mesmo excluir a matéria:', background_color='#2E2E2E',
                 justification='center',
                 relief='raised', border_width=3,
                 text_color='#58D3F7', font=('arial', 9))],
        [Sg.Text(arg, background_color='#2E2E2E', justification='center',
                 relief='raised', border_width=3,
                 text_color='#58D3F7', font=('arial', 9))],
        [Sg.Button('  Confirmar  ', size=(12, 0), border_width=4,
                   tooltip='  Se clicar aqui a matéria será excluída definitivamente!  ',
                   font=('arial', 9)),
         Sg.Button('  Cancelar  ', size=(12, 0), border_width=4,
                   tooltip='  Se clicar aqui a operação será cancelada!  ',
                   font=('arial', 9))
         ]
    ]
    confirm = Sg.FlexForm('Confirmação', element_justification='center').layout(layout3)
    event5, value5 = confirm.read()
    if event5 == '  Confirmar  ':
        confirm.close()
        return True
    if event5 == '  Cancelar  ':
        confirm.close()
        return False


def janela_inserir(color):
    c = color
    Sg.theme(c)
    layout0 = [
        [Sg.Text('Matéria >>', size=(12, 0), background_color='#2E2E2E'),
         Sg.InputText('', size=(51, 0), key='-disc-',
                      focus=True, border_width=4, background_color='#424242', text_color='#81F79F')],
        [Sg.Text('Semestre >>', size=(12, 0), background_color='#2E2E2E'),
         Sg.InputText('', size=(5, 0), key='-sm-',
                      border_width=4, background_color='#424242', text_color='#F4FA58'),
         Sg.Text('Simulado >>', size=(12, 0), background_color='#2E2E2E'),
         Sg.InputText('', size=(5, 0), key='-simu-',
                      border_width=4, background_color='#424242', text_color='#58ACFA'),
         Sg.Checkbox('<< Cálculo com duas notas', default=False, key='-calc-', visible=True,
                     tooltip='  Selecione para executar cálculo de média com apenas duas notas  ')],
        [Sg.Text('Prova 01 >>', size=(12, 0), background_color='#2E2E2E'),
         Sg.InputText('', size=(5, 0), key='-nota1-',
                      border_width=4, background_color='#424242', text_color='#58ACFA')],
        [Sg.Text('Prova 02 >>', size=(12, 0), background_color='#2E2E2E'),
         Sg.InputText('', size=(5, 0), key='-nota2-',
                      border_width=4, background_color='#424242', text_color='#58ACFA')],
        [Sg.Text('Prova 03 >>', size=(12, 0), background_color='#2E2E2E'),
         Sg.InputText('', size=(5, 0), key='-nota3-',
                      border_width=4, background_color='#424242', text_color='#58ACFA')],
        [Sg.Text('Prova 04 >>', size=(12, 0), background_color='#2E2E2E'),
         Sg.InputText('', size=(5, 0), key='-nota4-',
                      border_width=4, background_color='#424242', text_color='#58ACFA')],
        [Sg.Output(size=(84, 18), key='-out-', text_color='#00F5FF', background_color='#363636', visible=True)],
        [Sg.Button('Salvar', size=(10, 0), border_width=4,
                   tooltip='  Salvar  '),
         Sg.Button('Menu(<)', size=(10, 0), border_width=4,
                   tooltip='  Retornar ao menu de opções  ')]
    ]
    inserir = Sg.FlexForm('INSERIR').layout(layout0)
    zerar = 0
    while True:
        event0, value0 = inserir.read()
        if event0 == 'Menu(<)' or event0 == Sg.WIN_CLOSED:
            break
        if event0 == 'Salvar':
            dad0 = value0['-disc-']
            dad1 = value0['-sm-']
            dad2 = value0['-nota1-']
            dad3 = value0['-nota2-']
            dad4 = value0['-nota3-']
            dad5 = value0['-nota4-']
            dad6 = value0['-simu-']
            dad7 = value0['-calc-']
            up(inserir, '-disc-', '-sm-', '-nota1-', '-nota2-', '-nota3-',
               '-nota4-', '-simu-')
            b = media3.funtions.convert(dad0, dad1, dad2, dad3, dad4, dad5, dad6)
            a = media3.funtions.Banco(b[0], b[1], b[2], b[3], b[4], b[5], b[6], dad7)
            c = a.calcular_banco()
            d = media3.funtions.Banco.escrever(c[0], c[1], c[2], c[3], c[4], c[5],
                                               c[6], c[7], c[8], c[9], c[10], c[11],
                                               c[12], c[13], c[14], c[15])
            zerar += d
            if zerar == 5:
                zerar = 1
                up(inserir, '-out-')
    inserir.close()


def janela_update(color):
    c = color
    Sg.theme(c)
    c = media3.funtions.Banco()
    mat = c.carr_materias()
    layout1 = [
        [Sg.Text('Selecione a matéria >>', size=(24, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.InputCombo(mat,
                                                               background_color='#2E2E2E', text_color='#81F79F',
                                                               size=(51, 1), key='-comb-'),
         Sg.Button('ok', size=(2, 0), border_width=2,
                   tooltip='  Carregar dados!  ')],
        [Sg.Text('Matéria >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2),
         Sg.Text('',
                 size=(43, 0), background_color='#424242', text_color='#81F79F',
                 relief='sunken', border_width=2, key='-mat1-'),
         Sg.Text('Semestre >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2),
         Sg.Text('',
                 size=(5, 0), background_color='#424242', text_color='#F4FA58',
                 relief='sunken', border_width=2, key='-sm1-')],
        [Sg.Text('Prova 01 >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242', text_color='#58ACFA',
                                                         relief='sunken', border_width=2, key='-av1-'),
         Sg.Text('Prova 02 >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242', text_color='#58ACFA',
                                                         relief='sunken', border_width=2, key='-av2-'),
         Sg.Text('Prova 03 >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242', text_color='#58ACFA',
                                                         relief='sunken', border_width=2, key='-av3-'),
         Sg.Text('Prova 04 >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242', text_color='#58ACFA',
                                                         relief='sunken', border_width=2, key='-av4-')],
        [Sg.Text('Simulado >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242', text_color='#58ACFA',
                                                         relief='sunken', border_width=2, key='-sim-')],
        [Sg.Output(size=(84, 16), key='-out-', text_color='#00F5FF',
                   background_color='#363636', visible=True)],
        [Sg.Text('Simulado >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.InputText('',
                                                              size=(5, 0), background_color='#424242',
                                                              text_color='#01DF74',
                                                              border_width=4, key='-sim1-'),
         Sg.Text('', size=(49, 0), text_color='#0B615E',
                 relief='sunken', border_width=2, background_color='#2E2E2E', key='-out2-'),
         Sg.Text('', size=(5, 0), relief='sunken', border_width=2,
                 background_color='#2E2E2E', text_color='#FAAC58', justification='center', key='-tf-')],
        [Sg.Text('Prova 01 >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.InputText('',
                                                              size=(5, 0), background_color='#424242',
                                                              text_color='#01DF74',
                                                              border_width=4, key='-al1-'),
         Sg.Text('Prova 02 >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.InputText('',
                                                              size=(5, 0), background_color='#424242',
                                                              text_color='#01DF74',
                                                              border_width=4, key='-al2-'),
         Sg.Text('Prova 03 >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.InputText('',
                                                              size=(5, 0), background_color='#424242',
                                                              text_color='#01DF74',
                                                              border_width=4, key='-al3-'),
         Sg.Text('Prova 04 >>', size=(10, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.InputText('',
                                                              size=(5, 0), background_color='#424242',
                                                              text_color='#01DF74',
                                                              border_width=4, key='-al4-')],
        [Sg.Button('Alterar', size=(10, 0), border_width=4,
                   tooltip='  Salvar alterações  '),
         Sg.Button('Apagar', size=(10, 0), border_width=4,
                   tooltip='  Apaga registro do banco de dados  '),
         Sg.Button('Menu(<)', size=(10, 0), border_width=4,
                   tooltip='  Retornar ao menu de opções  ')]
    ]
    update = Sg.FlexForm('ALTERAR').layout(layout1)
    cm = bx = 83
    mat2 = None
    e = None
    while True:
        event1, value1 = update.read()
        if event1 == 'Menu(<)' or event1 == Sg.WIN_CLOSED:
            break
        if event1 == 'ok':
            if value1['-comb-'] != '':
                mat2 = value1['-comb-']
                if mat2 in mat:
                    e = c.carr_linha(mat2)
                    up1(update, '-mat1-', e[0], '-sm1-', e[1], '-av1-', e[2], '-av2-', e[3],
                        '-av3-', e[4], '-av4-', e[5], '-sim-', e[6])
                    update.find_element('-tf-').Update(e[7])
                    update.find_element('-out2-').Update(e[0])
                    up(update, '-comb-', '-out-')
                else:
                    up(update, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                       '-av3-', '-av4-', '-out-', '-out2-', '-tf-', '-sim-')
                    c.linhas('ERRO-Matéria inexistente no banco de dados!', cm, bx, 'ne')
            else:
                mat2 = ''
                up(update, '-comb-', '-mat1-', '-sm1-', '-av1-',
                   '-av2-', '-av3-', '-av4-', '-out-', '-out2-', '-tf-', '-sim-')
                c.linhas('ERRO-O campo referente à "Selecione a matéria" não pode ser vazio!', cm, bx, 'ne')
        if event1 == 'Alterar':
            if mat2 in mat:
                up(update, '-out-')
                px1 = value1['-al1-']
                px2 = value1['-al2-']
                px3 = value1['-al3-']
                px4 = value1['-al4-']
                px5 = value1['-sim1-']
                res = c.alter(px1, px2, px3, px4, px5, e[2], e[3], e[4], e[5], e[6])
                x = media3.funtions.Banco(e[0], e[1], res[0], res[1], res[2], res[3], res[4], e[7])
                y = x.calcular_banco()
                x.regrav(y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9], y[10],
                         y[11], y[12], y[13], y[14], y[15], e[0], res[5], res[6], res[7], res[8],
                         res[9], res[10], res[11], res[12], res[13], res[14])
                e = c.carr_linha(mat2)
                up1(update, '-mat1-', e[0], '-sm1-', e[1], '-av1-', e[2], '-av2-', e[3],
                    '-av3-', e[4], '-av4-', e[5], '-sim-', e[6])
                update.find_element('-tf-').Update(e[7])
                update.find_element('-out2-').Update(e[0])
            else:
                up(update, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                   '-av3-', '-av4-', '-out-', '-out2-', '-tf-', '-sim-')
                c.linhas('ERRO-Matéria inexistente no banco de dados!', cm, bx, 'ne')
        if event1 == 'Apagar':
            if mat2 in mat:
                cf = pop_confirm(mat2)
                if cf is True:
                    c.delete(mat2)
                    up(update, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                       '-av3-', '-av4-', '-out-', '-out2-', '-tf-', '-sim-')
                    mat = c.carr_materias()
                    c.linhas('SUCESSO-Matéria excluída do banco de dados!', cm, bx, 'ne')
                else:
                    mat2 = ''
                    up(update, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                       '-av3-', '-av4-', '-out-', '-out2-', '-tf-', '-sim-')
                    c.linhas('Operação abortada com sucesso!', cm, bx, 'ne')
            else:
                up(update, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                   '-av3-', '-av4-', '-out-', '-out2-', '-tf-', '-sim-')
                c.linhas('ERRO-Carregue uma matéria válida para depois excluíla!', cm, bx, 'ne')
    update.close()


def janela_visualizar(color):
    c = color
    cim = 91
    bi = 91
    e = None
    cnf = False
    Sg.theme(c)
    c = media3.funtions.Banco()
    mat = c.carr_materias()
    layout2 = [
        [Sg.Text('Média geral >>', size=(24, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(9, 0), background_color='#424242',
                                                         text_color='#9ACD32',
                                                         relief='sunken', border_width=2, key='-jk1-',
                                                         justification='right'),
         Sg.Text('Aproveitamentodo do curso até o momento >>', size=(41, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(9, 0), background_color='#424242',
                                                         text_color='#9ACD32',
                                                         relief='sunken', border_width=2, key='-jk100-',
                                                         justification='right'),
         Sg.Text('%', size=(0, 0), background_color='#424242',
                 relief='flat', border_width=2,
                 text_color='#9ACD32')],
        [linha22(95)],
        [Sg.Text('Selecione a matéria >>', size=(24, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2),
         Sg.InputCombo(mat,
                       background_color='#2E2E2E', text_color='#81F79F',
                       size=(51, 1), key='-comb-'),
         Sg.Button('ok', size=(13, 0), border_width=2,
                   tooltip='  Carregar dados!  ')],
        [Sg.Text('Filtrar por semestre >>', size=(24, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2),
         Sg.Checkbox('01',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(7, 0), key='-comb0-', default=False),
         Sg.Checkbox('02',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(7, 0), key='-comb1-', default=False),
         Sg.Checkbox('03',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(7, 0), key='-comb2-', default=False),
         Sg.Checkbox('04',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(7, 0), key='-comb3-', default=False),
         Sg.Checkbox('05',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(7, 0), key='-comb4-', default=False),
         Sg.Checkbox('06',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(7, 0), key='-comb5-', default=False)],
        [Sg.Text('Filtrar situação do aluno >>', size=(24, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2),
         Sg.Checkbox('Aprovado',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(9, 0), key='-comb6-', default=False),
         Sg.Checkbox('Ap. arred.',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(9, 0), key='-comb7-', default=False),
         Sg.Checkbox('Reprovado',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(9, 0), key='-comb8-', default=False),
         Sg.Checkbox('Cursando',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(9, 0), key='-comb9-', default=False),
         Sg.Checkbox('Indefinida',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(9, 0), key='-comb10-', default=False)],
        [Sg.Text('Filtrar situação  matéria >>', size=(24, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2),
         Sg.Checkbox('Concluída',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(9, 0), key='-comb11-', default=True),
         Sg.Checkbox('Em curso',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(9, 0), key='-comb12-', default=False),
         Sg.Checkbox('À cursar',
                     text_color='#A9F5F2', background_color='#2E2E2E',
                     size=(9, 0), key='-comb13-', default=False)],
        [Sg.Button('Relatório', size=(10, 0), border_width=4,
                   tooltip='  Apresenta relatório de todas as matérias, com ou sem filtros!  '),
         Sg.Button('Ranking', size=(10, 0), border_width=4,
                   tooltip='  Ordena as mtérias já concluídas em ordem decrescente  '),
         Sg.Button('Sem. inf.', size=(10, 0), border_width=4,
                   tooltip=' Mostra informações detalhadas de um determinado semestre '),
         Sg.Button('Notas ?', size=(10, 0), border_width=4,
                   tooltip=' Calcula as notas faltantes para atingir a média '),
         Sg.Button('Pesos', size=(10, 0), border_width=4,
                   tooltip=' Mostra o peso de cada nota na média final da metéria '),
         Sg.Button('Menu(<)', size=(10, 0), border_width=4,
                   tooltip='  Retornar ao menu de opções  ')],
        [Sg.Output(size=(92, 17), key='-out7-', text_color='#00F5FF',
                   background_color='#363636', visible=True)],
        [Sg.Text('Matéria >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2),
         Sg.Text('', size=(53, 0), background_color='#424242', text_color='#81F79F',
                 relief='sunken', border_width=2, key='-mat1-'),
         Sg.Text('Semestre >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2),
         Sg.Text('', size=(5, 0), background_color='#424242', text_color='#F4FA58',
                 relief='sunken', border_width=2, key='-sm1-')],
        [Sg.Text('Prova 01 >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242',
                                                         text_color='#58ACFA',
                                                         relief='sunken',
                                                         border_width=2, key='-av1-'),
         Sg.Text('Prova 02 >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242',
                                                         text_color='#58ACFA',
                                                         relief='sunken',
                                                         border_width=2, key='-av2-'),
         Sg.Text('Prova 03 >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2, key='-prv3-'), Sg.Text('',
                                                                       size=(5, 0), background_color='#424242',
                                                                       text_color='#58ACFA',
                                                                       relief='sunken',
                                                                       border_width=2, key='-av3-'),
         Sg.Text('Prova 04 >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2, key='-prv4-'), Sg.Text('',
                                                                       size=(5, 0), background_color='#424242',
                                                                       text_color='#58ACFA',
                                                                       relief='sunken',
                                                                       border_width=2, key='-av4-')],
        [Sg.Text('Média prova 01 >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242',
                                                         text_color='#F78181',
                                                         relief='sunken', border_width=2, key='-md1-'),
         Sg.Text('Média prova 02 >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242',
                                                         text_color='#F78181',
                                                         relief='sunken', border_width=2, key='-md2-'),
         Sg.Text('Média prova 03 >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2, key='-mgl3-'), Sg.Text('',
                                                                       size=(5, 0), background_color='#424242',
                                                                       text_color='#F78181',
                                                                       relief='sunken', border_width=2, key='-md3-'),
         Sg.Text('Média prova 04 >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2, key='-mgl4-'), Sg.Text('',
                                                                       size=(5, 0), background_color='#424242',
                                                                       text_color='#F78181',
                                                                       relief='sunken', border_width=2, key='-md4-')],
        [Sg.Text('Simulado >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242',
                                                         text_color='#58ACFA',
                                                         relief='sunken', border_width=2, key='-sim-'),
         Sg.Text('M.f. da matéria >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242',
                                                         text_color='#9F81F7',
                                                         relief='sunken', border_width=2, key='-mdfm-'),
         Sg.Text('Aproveitamento >>', size=(15, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242',
                                                         text_color='#9F81F7',
                                                         relief='sunken', border_width=2, key='-pda-'),
         Sg.Text('%', size=(0, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2,
                 text_color='#9F81F7'),
         Sg.Text('Tipo >>', size=(11, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('',
                                                         size=(5, 0), background_color='#424242',
                                                         text_color='#F7BE81', justification='center',
                                                         relief='sunken', border_width=2, key='-tp-')],
        [Sg.Text('Situação da matéria >>', size=(18, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('', justification='center',
                                                         size=(14, 0), background_color='#424242',
                                                         text_color='#F4FA58',
                                                         relief='sunken', border_width=2, key='-jk3-'),
         Sg.Text('Situação do aluno  >>', size=(18, 0), background_color='#2E2E2E',
                 relief='flat', border_width=2), Sg.Text('', justification='center',
                                                         size=(14, 0), background_color='#424242',
                                                         text_color='#81F79F',
                                                         relief='sunken', border_width=2, key='-jk4-')]
    ]
    visual = Sg.FlexForm('CÁLCULO MÉDIAS v 3.0').layout(layout2)
    while True:
        event2, value2 = visual.read()
        ag = c.x()
        ag1 = c.retiracasas1(ag[0], ag[1])
        up1(visual, '-jk1-', ag1[0], '-jk100-', ag1[1])
        if event2 == 'Menu(<)' or event2 == Sg.WIN_CLOSED:
            break
        if event2 == 'ok':
            if value2['-comb-'] != '':
                if value2['-comb-'] in mat:
                    try:
                        e = c.carr_linha0(value2['-comb-'])
                        x = c.retiracasas(e[0], e[1], e[2], e[3],
                                          e[4], e[5], e[6], e[7],
                                          e[8], e[9], e[10], e[11],
                                          e[12], e[13])
                    except Exception as erro:
                        up(visual, '-out7-')
                        print(erro)
                    else:
                        up(visual, '-out7-')
                        up1(visual, '-mat1-', x[0], '-sm1-', x[1], '-av1-', x[2], '-md1-', x[3],
                            '-av2-', x[4], '-md2-', x[5], '-av3-', x[6], '-md3-', x[7],
                            '-av4-', x[8], '-md4-', x[9], '-sim-', x[10], '-mdfm-', x[11],
                            '-pda-', x[12], '-tp-', x[13], '-jk3-', e[14], '-jk4-', e[15],
                            '-prv3-', 'lz', '-prv4-', 'lz', '-mgl3-', 'lz', '-mgl4-', 'lz')
                        up(visual, '-comb-')
                else:
                    up(visual, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                       '-av3-', '-av4-', '-md1-', '-md2-', '-md3-', '-md4-', '-mdfm-',
                       '-pda-', '-tp-', '-sim-', '-out7-', '-jk3-', '-jk4-')
                    c.linhas('ERRO-Matéria inexistente no banco de dados!', cim, bi, 'ne')
            else:
                e = None
                up(visual, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                   '-av3-', '-av4-', '-md1-', '-md2-', '-md3-', '-md4-', '-mdfm-',
                   '-pda-', '-tp-', '-out7-', '-sim-', '-jk3-', '-jk4-')
                c.linhas('ERRO-O campo referente à "Selecione a matéria" não pode ser vazio!', cim, bi, 'ne')
        if event2 == 'Notas ?':
            up(visual, '-out7-')
            if e is not None:
                if e[0] in mat:
                    up(visual, '-out7-')
                    cnf = True
                    c.informations(e[2], e[4], e[6], e[8], e[10], e[0], cnf)
                    cnf = False
                else:
                    up(visual, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                       '-av3-', '-av4-', '-md1-', '-md2-', '-md3-', '-md4-', '-mdfm-',
                       '-pda-', '-tp-', '-out7-', '-sim-', '-jk3-', '-jk4-')
                    c.linhas('ERRO-Matéria inexistente no banco de dados!', cim, bi, 'ne')
            else:
                up(visual, '-comb-', '-mat1-', '-sm1-', '-av1-', '-av2-',
                   '-av3-', '-av4-', '-md1-', '-md2-', '-md3-', '-md4-', '-mdfm-',
                   '-pda-', '-tp-', '-out7-', '-sim-', '-jk3-', '-jk4-')
                c.linhas('ERRO-É necessário carregar uma matéria válida para análise!', cim, bi, 'ne')
        if event2 == 'Pesos':
            up(visual, '-out7-')
            if e is not None:
                if e[0] in mat:
                    up(visual, '-out7-')
                    c.informations(e[2], e[4], e[6], e[8], e[10], e[0], cnf, True)
                else:
                    c.linhas('ERRO-Matéria inexistente no banco de dados!', cim, bi, 'ne')
            else:
                c.linhas('ERRO-É necessário carregar uma matéria válida para calcular o peso de cada nota!',
                         cim, bi, 'ne')
        if event2 == 'Relatório':
            up(visual, '-out7-')
            s1 = value2['-comb0-']
            s2 = value2['-comb1-']
            s3 = value2['-comb2-']
            s4 = value2['-comb3-']
            s5 = value2['-comb4-']
            s6 = value2['-comb5-']
            m1 = value2['-comb11-']
            m2 = value2['-comb12-']
            m3 = value2['-comb13-']
            a1 = value2['-comb6-']
            a2 = value2['-comb7-']
            a3 = value2['-comb8-']
            a4 = value2['-comb9-']
            a5 = value2['-comb10-']
            estatist = c.filtro(s1, s2, s3, s4, s5, s6,
                                m1, m2, m3,
                                a1, a2, a3, a4, a5)
            c.anime(visual, '-out7-', '=>', 3, 10, 'Reunindo as informações solicitadas')
            c.estat(estatist)
        if event2 == 'Ranking':
            c.anime(visual, '-out7-', '=>', 3, 10, 'Gerando placar')
            c.mostrar()
        if event2 == 'Sem. inf.':
            up(visual, '-out7-')
            k1 = value2['-comb0-']
            k2 = value2['-comb1-']
            k3 = value2['-comb2-']
            k4 = value2['-comb3-']
            k5 = value2['-comb4-']
            k6 = value2['-comb5-']
            c.anime(visual, '-out7-', '=>', 3, 10, 'Reunindo as informações solicitadas')
            c.medsem(k1, k2, k3, k4, k5, k6)
    visual.close()


def janela_opcao():
    Sg.theme('DarkGreen6')
    temas = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber',
             'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12',
             'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3',
             'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown',
             'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkGreen',
             'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGrey',
             'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7',
             'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5',
             'DarkPurple6', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1',
             'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5',
             'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging',
             'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1',
             'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7',
             'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12',
             'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5',
             'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1',
             'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3',
             'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8',
             'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3',
             'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal',
             'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Reddit',
             'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal',
             'Tan', 'TanBlue', 'TealMono', 'Topanga']
    n = media3.funtions.Banco
    layout4 = [
        [Sg.Text(' Bem vindo! ',
                 size=(28, 1), justification='center', font=('arial', 13),
                 background_color='#2E2E2E',
                 relief='raised', border_width=3,
                 text_color='#58D3F7')],
        [Sg.Text(' Escolha uma das opções abaixo. . . ',
                 size=(31, 0), justification='center',
                 background_color='#2E2E2E',
                 relief='raised', border_width=3,
                 text_color='#58D3F7')],
        [Sg.Button('  Módulo de inserção  ', size=(31, 0), border_width=4,
                   tooltip='  Inserir nova matéria no banco de dados!  ')],
        [Sg.Button('  Módulo de alteração  ', size=(31, 0), border_width=4,
                   tooltip='  Fazer alterações no banco de dados!  ')],
        [Sg.Button('  Módulo de visualização  ', size=(31, 0), border_width=4,
                   tooltip='  Visualizar resultados das suas provas!  ')],
        [Sg.Button('Sair', size=(31, 0), border_width=4,
                   tooltip='  Sair do sistema!  ')],
        [Sg.Text('', size=(31, 0), justification='center',
                 background_color='#2E2E2E',
                 relief='raised', border_width=3)],
        [Sg.InputOptionMenu(temas, size=(31, 0), default_value='DarkBlack1', key='-color-')]
    ]
    opcao4 = Sg.FlexForm('CÁLCULO MÉDIAS v 3.0', element_justification='center').layout(layout4)
    while True:
        event4, value4 = opcao4.read()
        c = value4['-color-']
        if event4 == 'Sair' or event4 == Sg.WIN_CLOSED:
            break
        if event4 == '  Módulo de inserção  ':
            n.criar()
            janela_inserir(c)
        if event4 == '  Módulo de alteração  ':
            janela_update(c)
        if event4 == '  Módulo de visualização  ':
            janela_visualizar(c)
    opcao4.close()
