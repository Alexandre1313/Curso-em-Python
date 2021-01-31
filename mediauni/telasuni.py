import PySimpleGUI as Sg
import mediauni.bduni


def tema():
    tems = Sg.theme('Darkblack')
    return tems


def janela_menu():
    tema()
    layout47 = [
        [Sg.Text('ESCOLHA UMA OPÇÃO ABAIXO', size=(58, 0))],
        [Sg.Button('RELATÓRIO', size=(58, 0))],
        [Sg.Button('ITERAÇÃO', size=(58, 0))],
        [Sg.Button('APROVEITAMENTO GERAL', size=(58, 0))],
        [Sg.Button('CADASTRAR', size=(58, 0))],
        [Sg.Button('EDITAR', size=(58, 0))],
        [Sg.Button('SAIR(x)', size=(58, 0))]
    ]
    menu = Sg.Window('MENU DE OPÇÕES', layout47, size=(410, 250), element_justification='center')
    while True:
        event21, value21 = menu.read()
        if event21 == 'SAIR(x)' or event21 == Sg.WIN_CLOSED:
            break
        if event21 == 'CADASTRAR':
            janela_cadastro()
        if event21 == 'EDITAR':
            janela_editar()
        if event21 == 'ITERAÇÃO':
            janela_vivo()
        if event21 == 'APROVEITAMENTO GERAL':
            janela_geral()
        if event21 == 'RELATÓRIO':
            janela_relatorio()
    menu.close()


def janela_inicio():
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
    tema()
    layout1 = [
        [Sg.Text('SEJA BEM VINDO!')],
        [Sg.Text('VAMOS ANALIZAR SUAS AVALIAÇÕES?')],
        [Sg.Button('ENTRAR(^)', size=(11, 0)), Sg.InputOptionMenu(temas, size=(11, 0))]
    ]
    inicio = Sg.Window('CÁLCULO MÉDIA v2.0', layout1, size=(400, 97), element_justification='center')
    event1, value1 = inicio.read()
    if event1 == 'ENTRAR(^)':
        mediauni.bduni.criar()
        inicio.close()
        janela_menu()
    if event1 == Sg.WIN_CLOSED:
        inicio.close()


def janela_final():
    tema()
    layout13 = [
        [Sg.Text('ATÉ BREVE!')],
        [Sg.Text('OBRIGADO VOLTE SEMPRE!')],
        [Sg.Button('Sair(x)', size=(16, 0))]
    ]
    final = Sg.Window('CÁLCULO MÉDIA v2.0', layout13, size=(400, 97), element_justification='center')
    event2, value2 = final.read()
    if event2 == 'Sair(x)' or event2 == Sg.WIN_CLOSED:
        final.close()


def linha23():
    linhas = '-' * 135
    print(linhas)


def janela_cadastro():
    tema()
    layout2 = [
        [Sg.Text('DISCIPLINA:', size=(12, 0)), Sg.InputText('', size=(71, 0), key='-disciplina-')],
        [mediauni.bduni.linha22(22)],
        [Sg.Text('AVALIAÇÃO 01:', size=(12, 0)), Sg.InputText('', size=(5, 0), key='-nota1-'),
         Sg.Text('AVALIAÇÃO 02:', size=(12, 0)), Sg.InputText('', size=(5, 0), key='-nota2-'),
         Sg.Text('AVALIAÇÃO 03:', size=(12, 0)), Sg.InputText('', size=(5, 0), key='-nota3-'),
         Sg.Text('AVALIAÇÃO 04:', size=(12, 0)), Sg.InputText('', size=(5, 0), key='-nota4-')],
        [mediauni.bduni.linha22(22)],
        [Sg.Button('Salvar', size=(10, 0)),
         Sg.Button('Tela menu(<)', size=(18, 0))]
    ]
    cadastro = Sg.Window('CADASTRO', layout2, size=(735, 160))
    while True:
        event16, value16 = cadastro.read()
        if event16 == 'Tela menu(<)' or event16 == Sg.WIN_CLOSED:
            break
        if event16 == 'Salvar':
            disciplina = value16['-disciplina-'].strip().title()
            nota1 = value16['-nota1-'].strip()
            nota2 = value16['-nota2-'].strip()
            nota3 = value16['-nota3-'].strip()
            nota4 = value16['-nota4-'].strip()
            valores = [nota1, nota2, nota3, nota4]
            valores0 = []
            if disciplina != '':
                try:
                    for v in valores:
                        floo = float(v)
                        valores0.append(floo)
                except(ValueError, TypeError):
                    mediauni.bduni.up(cadastro, '-nota1-', '-nota2-', '-nota3-', '-nota4-', '-disciplina-')
                    Sg.popup_auto_close('ERRO! Os campos "AVALIAÇÃO" só podem conter números')
                else:
                    dado2 = mediauni.bduni.atuliz()
                    if (10 >= valores0[0] >= 0 and 10 >= valores0[1] >= 0
                            and 10 >= valores0[2] >= 0 and 10 >= valores0[3] >= 0):
                        if disciplina not in dado2:
                            mediauni.bduni.escrever(disciplina, valores0[0], valores0[1], valores0[2], valores0[3])
                            mediauni.bduni.up(cadastro, '-nota1-', '-nota2-', '-nota3-', '-nota4-', '-disciplina-')
                            Sg.popup_auto_close('OK! Informações inseridas no banco de dados com sucesso')
                        else:
                            mediauni.bduni.up(cadastro, '-nota1-', '-nota2-', '-nota3-', '-nota4-', '-disciplina-')
                            Sg.popup_auto_close('ERRO! Erro ao inserir informações no banco de dados')
                    else:
                        mediauni.bduni.up(cadastro, '-nota1-', '-nota2-', '-nota3-', '-nota4-', '-disciplina-')
                        Sg.popup_auto_close('ERRO! Uma ou mais notas é > 10 ou < 0')
            else:
                mediauni.bduni.up(cadastro, '-nota1-', '-nota2-', '-nota3-', '-nota4-', '-disciplina-')
                Sg.popup_auto_close('ERRO! O campo "DISCIPLINA" não pode ser vazio')
    cadastro.close()


def janela_editar():
    tema()
    dado2 = mediauni.bduni.atuliz()
    layout4 = [
        [Sg.Text('CARREGAR NOTAS À SEREM ALTERADAS')],
        [Sg.Text('Disciplina>>', size=(11, 0)), Sg.InputCombo(dado2, size=(37, 1), key='-comb-'),
         Sg.Button('Carregar...', size=(10, 0))],
        [mediauni.bduni.linha22(22)],
        [Sg.Text('Disc. >>', size=(6, 0)), Sg.Text('', size=(37, 0), key='-dmos-')],
        [Sg.Text('Avaliação 1 >>', size=(11, 0)), Sg.Text('', size=(5, 0), key='-n1-'),
         Sg.Text('Avaliação 2 >>', size=(11, 0)), Sg.Text('', size=(5, 0), key='-n2-'),
         Sg.Text('Avaliação 3 >>', size=(11, 0)), Sg.Text('', size=(5, 0), key='-n3-'),
         Sg.Text('Avaliação 4 >>', size=(11, 0)), Sg.Text('', size=(5, 0), key='-n4-')],
        [mediauni.bduni.linha22(22)],
        [Sg.Text('INFORME AS NOVAS NOTAS')],
        [Sg.Text('Edit nota 1 >>', size=(11, 0)), Sg.Input('', size=(5, 0), key='-e1-'),
         Sg.Text('Edit nota 2 >>', size=(11, 0)), Sg.Input('', size=(5, 0), key='-e2-'),
         Sg.Text('Edit nota 3 >>', size=(11, 0)), Sg.Input('', size=(5, 0), key='-e3-'),
         Sg.Text('Edit nota 4 >>', size=(11, 0)), Sg.Input('', size=(5, 0), key='-e4-')],
        [Sg.Button('Salvar Alterações', size=(18, 0))],
        [mediauni.bduni.linha22(22)],
        [Sg.Text('EXCLUIR REGISTRO DO BANCO DE DADOS')],
        [Sg.Text('Disciplina>>', size=(11, 0)), Sg.InputCombo(dado2, size=(37, 1), key='-comb1-')],
        [Sg.Button('Deletar', size=(18, 0))],
        [mediauni.bduni.linha22(22)],
        [Sg.Output(size=(85, 9), key='-out-')],
        [Sg.Text('', size=(58, 0)), Sg.Button('Tela menu(<)', size=(18, 0))],
    ]
    editar = Sg.Window('EDITAR', layout4, size=(735, 600))
    while True:
        event17, value17 = editar.read()
        if event17 == 'Tela menu(<)' or event17 == Sg.WIN_CLOSED:
            break
        dado3 = []
        if event17 == 'Carregar...':
            vari1 = value17['-comb-']
            if vari1:
                if vari1 in dado2:
                    dado1 = mediauni.bduni.lertab0(vari1)
                    mediauni.bduni.up(editar, '-out-')
                    for d in dado1:
                        for v in d:
                            dado3.append(v)
                    editar.find_element('-dmos-').Update(dado3[0])
                    editar.find_element('-n1-').Update(dado3[1])
                    editar.find_element('-n2-').Update(dado3[2])
                    editar.find_element('-n3-').Update(dado3[3])
                    editar.find_element('-n4-').Update(dado3[4])
                else:
                    mediauni.bduni.up(editar, '-comb-')
                    Sg.popup_auto_close('ERRO! Disciplina inexistente no banco de dados')
            else:
                Sg.popup_auto_close('ERRO! Selecione uma disciplina para carregar os dados')
        if event17 == 'Salvar Alterações':
            vari2 = value17['-comb-']
            if vari2:
                not1 = value17['-e1-']
                not2 = value17['-e2-']
                not3 = value17['-e3-']
                not4 = value17['-e4-']
                dad = {'a1': not1, 'a2': not2, 'a3': not3, 'a4': not4}
                try:
                    for k, v in dad.items():
                        if v != '':
                            dad1 = float(v)
                            if 10 >= dad1 >= 0:
                                dad[k] = dad1
                            else:
                                dad[k] = ''
                except(ValueError, TypeError):
                    Sg.popup_auto_close('ERRO! Os campos de alteração só podem conter números')
                else:
                    cont = 0
                    for k, v in dad.items():
                        if v != '' and 10 >= v >= 0:
                            if k == 'a1':
                                cont += 1
                                mediauni.bduni.alterar1(v, vari2)
                                print(f'Alterações na disciplina "{vari2}" no campo "NOTA{cont}" realizada'
                                      f' com sucesso!')
                            if k == 'a2':
                                cont += 1
                                mediauni.bduni.alterar2(v, vari2)
                                print(f'Alterações na disciplina "{vari2}" no campo "NOTA{cont}" realizada'
                                      f' com sucesso!')
                            if k == 'a3':
                                cont += 1
                                mediauni.bduni.alterar3(v, vari2)
                                print(f'Alterações na disciplina "{vari2}" no campo "NOTA{cont}" realizada'
                                      f' com sucesso!')
                            if k == 'a4':
                                cont += 1
                                mediauni.bduni.alterar4(v, vari2)
                                print(f'Alterações na disciplina "{vari2}" no campo "NOTA{cont}" realizada'
                                      f' com sucesso!')
                        else:
                            cont += 1
                            print(f'Alterações na disciplina "{vari2}" no campo "NOTA{cont}"  NÂO realizada !'
                                  f' NOTA > 10 ou NOTA < 0 ou "  ".')
                    mediauni.bduni.up(editar, '-e1-', '-e2-', '-e3-', '-e4-', '-comb-')
            else:
                mediauni.bduni.up(editar, '-out-')
                Sg.popup_auto_close('ERRO! Selecione uma disciplina para alterar os dados')
        if event17 == 'Deletar':
            dado2 = mediauni.bduni.atuliz()
            vari3 = value17['-comb1-']
            if vari3:
                if vari3 in dado2:
                    mediauni.bduni.delete(vari3)
                    mediauni.bduni.up(editar, '-n1-', '-n2-', '-n3-', '-n4-', '-comb-', '-comb1-', '-dmos-')
                    print('Linha de dados excluída com sucesso!')
                    Sg.popup_auto_close('Linha de dados excluída com sucesso!')
                    dado2 = mediauni.bduni.atuliz()
                else:
                    mediauni.bduni.up(editar, '-comb1-')
                    print('ERRO! Disciplina não encontrada no banco de dados')
                    Sg.popup_auto_close('ERRO! Disciplina não encontrada no banco de dados')
            else:
                mediauni.bduni.up(editar, '-comb1-')
                print('ERRO! Selecione uma disciplina para exclusão')
                Sg.popup_auto_close('ERRO! Selecione uma disciplina para exclusão')
    editar.close()


def janela_vivo():
    tema()
    dado2 = mediauni.bduni.atuliz()
    layout94 = [
        [Sg.Text('Avaliação 01', size=(10, 0)), Sg.Input('', size=(5, 0), key='-n1-'),
         Sg.Button('Obter informações da prova 01'),
         Sg.Button('Nota 1?', size=(7, 0)), Sg.InputCombo(dado2, size=(25, 1), key='-comb3-')],
        [Sg.Text('Avaliação 02', size=(10, 0)), Sg.Input('', size=(5, 0), key='-n2-'),
         Sg.Button('Obter informações da prova 02'),
         Sg.Button('Nota 2?', size=(7, 0)), Sg.Button('Carregar...', size=(13, 0))],
        [Sg.Text('Avaliação 03', size=(10, 0)), Sg.Input('', size=(5, 0), key='-n3-'),
         Sg.Button('Obter informações da prova 03'),
         Sg.Button('Nota 3?', size=(7, 0)), Sg.Button('Limpar dados', size=(13, 0))],
        [Sg.Text('Avaliação 04', size=(10, 0)), Sg.Input('', size=(5, 0), key='-n4-'),
         Sg.Button('Obter informações da prova 04'),
         Sg.Button('Nota 4?', size=(7, 0))],
        [Sg.Button('Relatório', size=(10, 0)), Sg.Button('Situação', size=(10, 0)),
         Sg.Button('Média Final', size=(10, 0)), Sg.Button('Pesos', size=(10, 0))],
        [mediauni.bduni.linha22(22)],
        [Sg.Text('', size=(18, 0), key='-discarr1-'), Sg.Text('', size=(37, 0), key='-discarr-')],
        [Sg.Output(size=(85, 22), key='-out2-')],
        [Sg.Button('Tela menu(<)', size=(18, 0))]
    ]
    vivo1 = Sg.Window('ITERAÇÃO', layout94, size=(735, 650))
    while True:
        event18, values18 = vivo1.read()
        if event18 == 'Tela menu(<)' or event18 == Sg.WIN_CLOSED:
            break
        if values18['-n1-'] != '' and values18['-n2-'] != '' and values18['-n3-'] != '' and values18['-n4-'] != '':
            lista = list()
            try:
                not1 = values18['-n1-']
                not2 = values18['-n2-']
                not3 = values18['-n3-']
                not4 = values18['-n4-']
                dad = {'f1': not1, 'f2': not2, 'f3': not3, 'f4': not4}
                for v in dad.values():
                    valor = float(v)
                    lista.append(valor)
            except(ValueError, TypeError):
                print()
                mediauni.bduni.up(vivo1, '-out2-')
                print('ERRO-Valor inválido!Verifique')
                linha23()
            else:
                media7 = 7.0
                media8 = 10
                media6 = media9 = 6.52
                media1 = lista[0] * 1.5 / 10
                media2 = lista[1] * 1.5 / 10
                media3 = lista[2] * 3.0 / 10
                media4 = lista[3] * 4.0 / 10
                mediamom = (media1 + media2 + media3 + media4)
                if event18 == 'Obter informações da prova 01':
                    mediauni.bduni.up(vivo1, '-out2-')
                    if 10 >= lista[0] >= 0:
                        print(f'{"INFORMAÇÕES REFERENTE À PROVA 01:":<50}')
                        print()
                        print(f'Nota   obtida na prova 01 =  {lista[0]:.2f}')
                        print(f'Média obtida na prova 01 =  {media1:.3f}')
                        if mediamom > 0:
                            print(
                                f'Peso da prova 01 na média (pontos percentuais)   =   {media1 * 100 / mediamom:.1f} %')
                        else:
                            print(f'Cálculo do peso da prova 01 indisponível, pois a média tem valor = 0! Verifique ')
                        print()
                        linha23()
                    else:
                        print(f'ERRO-A nota informada, no caso a nota  {lista[0]}  não é válida! Verifique')
                        print()
                        linha23()
                if event18 == 'Obter informações da prova 02':
                    if 10 >= lista[1] >= 0:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"INFORMAÇÕES REFERENTE À PROVA 02:":<50}')
                        print()
                        print(f'Nota   obtida na prova 02 =  {lista[1]:.2f}')
                        print(f'Média obtida na prova 02 =  {media2:.3f}')
                        if mediamom > 0:
                            print(
                                f'Peso da prova 02 na média (pontos percentuais)   =   {media2 * 100 / mediamom:.1f} %')
                        else:
                            print(f'Cálculo do peso da prova 01 indisponível, pois a média tem valor = 0! Verifique ')
                        print()
                        linha23()
                    else:
                        print(f'ERRO-A nota informada, no caso a nota  {lista[1]}  não é válida! Verifique')
                        print()
                        linha23()
                if event18 == 'Obter informações da prova 03':
                    if 10 >= lista[2] >= 0:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"INFORMAÇÕES REFERENTE À PROVA 03:":<50}')
                        print()
                        print(f'Nota   obtida na prova 03 =  {lista[2]:.2f}')
                        print(f'Média obtida na prova 03 =  {media3:.3f}')
                        if mediamom > 0:
                            print(
                                f'Peso da prova 03 na média (pontos percentuais)   =   {media3 * 100 / mediamom:.1f} %')
                        else:
                            print(f'Cálculo do peso da prova 01 indisponível, pois a média tem valor = 0! Verifique ')
                        print()
                        linha23()
                    else:
                        print(f'ERRO-A nota informada, no caso a nota  {lista[2]}  não é válida! Verifique')
                        print()
                        linha23()
                if event18 == 'Obter informações da prova 04':
                    if 10 >= lista[3] >= 0:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"INFORMAÇÕES REFERENTE À PROVA 04:":<50}')
                        print()
                        print(f'Nota   obtida na prova 04 =  {lista[3]:.2f}')
                        print(f'Média obtida na prova 04 =  {media4:.3f}')
                        if mediamom > 0:
                            print(
                                f'Peso da prova 04 na média (pontos percentuais)   =   {media4 * 100 / mediamom:.1f} %')
                        else:
                            print(f'Cálculo do peso da prova 01 indisponível, pois a média tem valor = 0! Verifique ')
                        print()
                        linha23()
                    else:
                        print(f'ERRO-A nota informada, no caso a nota  {lista[3]}  não é válida! Verifique')
                        print()
                        linha23()
                if event18 == 'Relatório':
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"MÉDIA / FALTAS / SOBRAS (PONTOS):":<50}')
                        print()
                        print(f'Média conquistada   =   {mediamom:.3f}')
                        if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                            if mediamom < media7:
                                print(f'Falta para atingir a média 7,0   =   {media7 - mediamom:.2f}')
                            elif mediamom == media7:
                                print(
                                    f'Não houve sobras nem faltas em relação à média 7,0   =   {mediamom - media7:.2f}')
                            else:
                                print(f'Você já atingiu a média 7,0 e ultrapassou   =   {mediamom - media7:.2f}')
                        if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                            if mediamom < media6:
                                sd1 = media6 - mediamom
                                print(f'Falta para atingir a media 6,52 para arredondamento   =   {sd1:.2f}')
                            elif mediamom == media6:
                                print(f'Não houve sobras nem faltas em relação à média 6,52 para arredondamento   '
                                      f'=   {mediamom - media6:.2f}')
                            else:
                                print(f'Você já atingiu a média 6,52 para arredondamento e ultrapassou   '
                                      f'=   {mediamom - media6:.2f}')
                        print()
                        linha23()
                        print(f'{"PERCENTUAIS JÁ CONQUISTADOS:":<50}')
                        print()
                        print(f'Percentual já atingido em relação ao curso   =   {mediamom * 100 / 10:.1f} %')
                        print(f'Percentual já atingido em relação à média 7,0   =   {mediamom * 100 / media7:.1f} %')
                        print(f'Percentual já atingido em relação à média 6,52 (para '
                              f'arredondamento)   =   {mediamom * 100 / media6:.1f} %')
                        print()
                        linha23()
                        if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                            print(f'{"FALTA / SOBRAS (PERCENTUAIS):":<50}')
                            print()
                            print(
                                f'Percentual faltante em relação ao curso   =   {(media8 - mediamom) * 100 / 10:.1f} %')
                        if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                            if (media7 - mediamom) * 100 / media7 > 0:
                                print(f'Percentual faltante em relação à média 7,0   =   '
                                      f'{(media7 - mediamom) * 100 / media7:.1f} %')
                            elif (media7 - mediamom) * 100 / media7 == 0:
                                print(f'Não houve faltas ou sobras em relação à média 7,0   =   '
                                      f'{(media7 - mediamom) * 100 / media7:.1f} %')
                            else:
                                sd0 = (media7 - mediamom) * 100 / media7 - (media7 - mediamom) * 100 / media7 * 2
                                print(f'Você ultrapassou a média 7,0 em   =   {sd0:.1f} %')
                        if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                            if (media9 - mediamom) * 100 / media6 > 0:
                                print(f'Percentual faltante em relação à média 6,52 (Para arredondamento)   =   '
                                      f'{(media9 - mediamom) * 100 / media6:.1f} %')
                            elif (media9 - mediamom) * 100 / media6 == 0:
                                print(f'Não houve faltas ou sobras em relação à média 6,52 (Para arredondamento)   =   '
                                      f'{(media9 - mediamom) * 100 / media6:.1f} %')
                            else:
                                sd = (media9 - mediamom) * 100 / media6 - (media9 - mediamom) * 100 / media6 * 2
                                print(f'Você ultrapassou a média 6,52 (Para arredondamento) em   =   {sd:.1f} %')
                        print()
                        linha23()
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print('ERRO-As notas informadas não geram uma média válida! Verifique')
                        print()
                        linha23()
                if event18 == 'Nota 1?':
                    if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                            and lista[0] == 0):
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"NOTA PENDENTE PROVA 01 (PARA APROVAÇÃO COM MÉDIA 7,0):":<50}')
                        print()
                        var7 = (media7 - mediamom) * 10 / 1.5
                        if 10 >= var7 >= 0:
                            print(f'Para aprovação com média 7,0 você precisa tirar   =   {var7:.2f}')
                        elif var7 > 10:
                            print(f'Já não há o que fazer, tente a nota por arredondamento')
                        else:
                            print(f'Nota não necessária para aprovação ==> JÁ APROVADO')
                        print()
                        linha23()
                    if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                            and lista[0] == 0):
                        print(f'{"NOTA PENDENTE PROVA 01 (PARA APROVAÇÃO COM MÉDIA 6,52 (ARREDONDAMENTO)):":<50}')
                        print()
                        var6 = (media6 - mediamom) * 10 / 1.5
                        if 10 >= var6 >= 0:
                            print(f'Para aprovação com média 6,52 (Para arredondamento) '
                                  f'você precisa tirar   =   {var6:.2f}')
                        elif var6 > 10:
                            print(f'Já não há o que fazer, pois necessitaria de um   =   {var6:.2f}')
                        else:
                            print('Nota não necessária para aprovação ==> JÁ APROVADO')
                        print()
                        linha23()
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 01 '
                              f'é diferente de 0!')
                        print()
                        linha23()
                if event18 == 'Nota 2?':
                    if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                            and lista[1] == 0):
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"NOTA PENDENTE PROVA 02 (PARA APROVAÇÃO COM MÉDIA 7,0):":<50}')
                        print()
                        var7 = (media7 - mediamom) * 10 / 1.5
                        if 10 >= var7 >= 0:
                            print(f'Para aprovação com média 7,0 você precisa tirar   =   {var7:.2f}')
                        elif var7 > 10:
                            print(f'Já não há o que fazer, tente a nota por arredondamento')
                        else:
                            print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 02 '
                                  f'é diferente de 0!')
                        print()
                        linha23()
                    if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                            and lista[1] == 0):
                        print(f'{"NOTA PENDENTE PROVA 02 (PARA APROVAÇÃO COM MÉDIA 6,52 (ARREDONDAMENTO)):":<50}')
                        print()
                        var6 = (media6 - mediamom) * 10 / 1.5
                        if 10 >= var6 >= 0:
                            print(f'Para aprovação com média 6,52 (Para arredondamento) '
                                  f'você precisa tirar   =   {var6:.2f}')
                        elif var6 > 10:
                            print(f'Já não há o que fazer, pois necessitaria de um   =   {var6:.2f}')
                        else:
                            print('Nota não necessária para aprovação ==> JÁ APROVADO')
                        print()
                        linha23()
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 02 '
                              f'é diferente de 0!')
                        print()
                        linha23()
                if event18 == 'Nota 3?':
                    if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                            and lista[2] == 0):
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"NOTA PENDENTE PROVA 03 (PARA APROVAÇÃO COM MÉDIA 7,0):":<50}')
                        print()
                        var7 = (media7 - mediamom) * 10 / 3.0
                        if 10 >= var7 >= 0:
                            print(f'Para aprovação com média 7,0 você precisa tirar   =   {var7:.2f}')
                        elif var7 > 10:
                            print(f'Já não há o que fazer, tente a nota por arredondamento')
                        else:
                            print(f'Nota não necessária para aprovação ==> JÁ APROVADO')
                        print()
                        linha23()
                    if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                            and lista[2] == 0):
                        print(f'{"NOTA PENDENTE PROVA 03 (PARA APROVAÇÃO COM MÉDIA 6,52 (ARREDONDAMENTO)):":<50}')
                        print()
                        var6 = (media6 - mediamom) * 10 / 3.0
                        if 10 >= var6 >= 0:
                            print(f'Para aprovação com média 6,52 (Para arredondamento) '
                                  f'você precisa tirar   =   {var6:.2f}')
                        elif var6 > 10:
                            print(f'Já não há o que fazer, pois necessitaria de um   =   {var6:.2f}')
                        else:
                            print('Nota não necessária para aprovação ==> JÁ APROVADO')
                        print()
                        linha23()
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 03 '
                              f'é diferente de 0!')
                        print()
                        linha23()
                if event18 == 'Nota 4?':
                    if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                            and lista[3] == 0):
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"NOTA PENDENTE PROVA 04 (PARA APROVAÇÃO COM MÉDIA 7,0):":<50}')
                        print()
                        var7 = (media7 - mediamom) * 10 / 4.0
                        if 10 >= var7 >= 0:
                            print(f'Para aprovação com média 7,0 você precisa tirar   =   {var7:.2f}')
                        elif var7 > 10:
                            print(f'Já não há o que fazer, tente a nota por arredondamento')
                        else:
                            print(f'Nota não necessária para aprovação ==> JÁ APROVADO')
                        print()
                        linha23()
                    if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                            and lista[3] == 0):
                        print(f'{"NOTA PENDENTE PROVA 04 (PARA APROVAÇÃO COM MÉDIA 6,52 (ARREDONDAMENTO)):":<50}')
                        print()
                        var6 = (media6 - mediamom) * 10 / 4.0
                        if 10 >= var6 >= 0:
                            print(f'Para aprovação com média 6,52 (Para arredondamento) '
                                  f'você precisa tirar   =   {var6:.2f}')
                        elif var6 > 10:
                            print(f'Já não há o que fazer, pois necessitaria de um   =   {var6:.2f}')
                        else:
                            print('Nota não necessária para aprovação ==> JÁ APROVADO')
                        print()
                        linha23()
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 04 '
                              f'é diferente de 0!')
                        print()
                        linha23()
                if event18 == 'Média Final':
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"SUA MÉDIA FINAL: ":<50}')
                        print()
                        if lista[0] == 0 and lista[1] > 0 and lista[2] > 0 and lista[3] > 0:
                            print(f'Sua média final foi (Prova 01 não obteve pontos > 0)   =   {mediamom:.2f}')
                            print()
                            linha23()
                        elif lista[0] > 0 and lista[1] == 0 and lista[2] > 0 and lista[3] > 0:
                            print(f'Sua média final foi (Prova 02 não obteve pontos > 0)   =   {mediamom:.2f}')
                            print()
                            linha23()
                        elif lista[0] > 0 and lista[1] > 0 and lista[2] == 0 and lista[3] > 0:
                            print(f'Sua média final foi (Prova 03 não obteve pontos > 0)   =   {mediamom:.2f}')
                            print()
                            linha23()
                        elif lista[0] > 0 and lista[1] > 0 and lista[2] > 0 and lista[3] == 0:
                            print(f'Sua média final foi (Prova 04 não obteve pontos > 0)   =   {mediamom:.2f}')
                            print()
                            linha23()
                        elif lista[0] > 0 and lista[1] > 0 and lista[2] > 0 and lista[3] > 0:
                            print(f'Sua média final foi (Todas as provas possuem valor > 0)   =   {mediamom:.2f}')
                            print()
                            linha23()
                        else:
                            print(f'ERRO-Média final não disponível, pois mais de uma prova esta com valor = 0'
                                  f'! Verifique')
                            print()
                            linha23()
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print('ERRO-As notas informadas não geram uma média válida! Verifique')
                        print()
                        linha23()
                if event18 == 'Situação':
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"SITUAÇÃO: ":<50}')
                        print()
                        if (lista[0] == 0 and lista[1] > 0 and lista[2] > 0 and lista[3] > 0 or
                                lista[0] > 0 and lista[1] == 0 and lista[2] > 0 and lista[3] > 0 or
                                lista[0] > 0 and lista[1] > 0 and lista[2] == 0 and lista[3] > 0 or
                                lista[0] > 0 and lista[1] > 0 and lista[2] > 0 and lista[3] == 0 or
                                lista[0] > 0 and lista[1] > 0 and lista[2] > 0 and lista[3] > 0):
                            if mediamom >= media7:
                                print(f'APROVADO!!! COM MÉDIA   =   {mediamom:.2f}')
                                print()
                                linha23()
                            elif media7 > mediamom >= media6:
                                print(f'APROVADO, POR ARREDONDAMENTO!! COM MÉDIA   =   {mediamom:.2f}')
                                print()
                                linha23()
                            else:
                                print(f'REPROVADO! COM MÉDIA   =   {mediamom:.2f}')
                                print()
                                linha23()
                        else:
                            print(f'ERRO-Não é possível verificar sua situação, pois mais de uma prova esta com'
                                  f' valor = 0! Verifique')
                            print()
                            linha23()
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print('ERRO-As notas informadas não geram uma média válida! Verifique')
                        print()
                        linha23()
                if event18 == 'Pesos':
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print(f'{"PESO DE CADA PROVA NA MÉDIA FINAL OBTIDA:":<50}')
                        print()
                        if (lista[0] == 0 and lista[1] > 0 and lista[2] > 0 and lista[3] > 0 or
                                lista[0] > 0 and lista[1] == 0 and lista[2] > 0 and lista[3] > 0 or
                                lista[0] > 0 and lista[1] > 0 and lista[2] == 0 and lista[3] > 0 or
                                lista[0] > 0 and lista[1] > 0 and lista[2] > 0 and lista[3] == 0 or
                                lista[0] > 0 and lista[1] > 0 and lista[2] > 0 and lista[3] > 0):
                            print(f'A prova 01 teve um peso em sua media final (em pontos percentuais) de   =   '
                                  f'{media1 * 100 / mediamom:.1f} %')
                            print(f'A prova 02 teve um peso em sua media final (em pontos percentuais) de   =   '
                                  f'{media2 * 100 / mediamom:.1f} %')
                            print(f'A prova 03 teve um peso em sua media final (em pontos percentuais) de   =   '
                                  f'{media3 * 100 / mediamom:.1f} %')
                            print(f'A prova 04 teve um peso em sua media final (em pontos percentuais) de   =   '
                                  f'{media4 * 100 / mediamom:.1f} %')
                            print()
                            linha23()
                        else:
                            print(f'ERRO-Não é possível verificar o peso de cada prova, pois mais de uma prova esta com'
                                  f' valor = 0!')
                            print()
                            linha23()
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print('ERRO-As notas informadas não geram uma média válida! Verifique')
                        print()
                        linha23()
        else:
            if event18 == 'Carregar...':
                vari4 = values18['-comb3-']
                if vari4:
                    if vari4 in dado2:
                        mediauni.bduni.up(vivo1, '-discarr1-', '-discarr-', '-out2-', '-n1-', '-n2-', '-n3-', '-n4-')
                        dado0 = mediauni.bduni.aluliz1(vari4)
                        vivo1.find_element('-discarr1-').Update('Disciplina carregada >>')
                        vivo1.find_element('-discarr-').Update(dado0[0].capitalize())
                        vivo1.find_element('-n1-').Update(dado0[1])
                        vivo1.find_element('-n2-').Update(dado0[2])
                        vivo1.find_element('-n3-').Update(dado0[3])
                        vivo1.find_element('-n4-').Update(dado0[4])
                        mediauni.bduni.up(vivo1, '-comb3-')
                    else:
                        mediauni.bduni.up(vivo1, '-out2-')
                        print()
                        print('Disciplina não encontrada no banco de dados!')
                        linha23()
                else:
                    mediauni.bduni.up(vivo1, '-out2-')
                    print()
                    print('ERRO-Selecione uma disciplina para acarregar notas do banco de dados!')
                    linha23()
            else:
                mediauni.bduni.up(vivo1, '-out2-')
                print()
                print('ERRO-Nenhum campo de entrada pode ser vazio!Verifique')
                linha23()
        if event18 == 'Limpar dados':
            mediauni.bduni.up(vivo1, '-comb3-', '-discarr1-', '-discarr-', '-out2-', '-n1-', '-n2-', '-n3-', '-n4-')
    vivo1.close()


def janela_geral():
    tema()
    layout29 = [
        [Sg.Text('Média de aproveitamento geral >>', size=(26, 0)),
         Sg.Text('', size=(37, 0)), Sg.Text('', size=(5, 0), key='-gr-'),
         Sg.Text('%')],
        [Sg.Text('Disc. + >>', size=(26, 0)), Sg.Text('', size=(37, 0), key='-dmai-'),
         Sg.Text('', size=(5, 0), key='-nma-'), Sg.Text('%')],
        [Sg.Text('Disc. - >>', size=(26, 0)), Sg.Text('', size=(37, 0), key='-dmen-'),
         Sg.Text('', size=(5, 0), key='-nme-'), Sg.Text('%')],
        [Sg.Output(size=(85, 29), key='-out-')],
        [Sg.Button('Gerar', size=(10, 0)), Sg.Text('', size=(46, 0)),
         Sg.Button('Tela menu(<)', size=(18, 0))]
    ]
    geral = Sg.Window('APROVEITAMENTO GERAL', layout29, size=(735, 630))
    while True:
        event19, value19 = geral.read()
        if event19 == 'Tela menu(<)' or event19 == Sg.WIN_CLOSED:
            break
        if event19 == 'Gerar':
            mediauni.bduni.up(geral, '-out-')
            dado = mediauni.bduni.atuliz0()
            md = mediauni.bduni.aproveitamento(dado)
            geral.find_element('-gr-').Update(f'{md[0]:.1f}')
            geral.find_element('-dmai-').Update(md[1].capitalize())
            geral.find_element('-nma-').Update(f'{md[2]:.1f}')
            geral.find_element('-dmen-').Update(md[3].capitalize())
            geral.find_element('-nme-').Update(f'{md[4]:.1f}')
    geral.close()


def janela_relatorio():
    tema()
    dado2 = mediauni.bduni.atuliz()
    layout3 = [
        [Sg.Text('Disciplina >>', size=(11, 0)), Sg.InputCombo(dado2, size=(37, 1), key='-comb-')],
        [Sg.Button('Relatório', size=(10, 0)), Sg.Text('<< Gerar relatório final', size=(17, 0)),
         Sg.Text('Média final >>', size=(10, 0)), Sg.Text('', size=(5, 0), key=['-tf-'])],
        [Sg.Text('Avaliação 1 >>', size=(11, 0)), Sg.Text('', size=(5, 0), key='-n1-'),
         Sg.Text('Avaliação 2 >>', size=(11, 0)), Sg.Text('', size=(5, 0), key='-n2-'),
         Sg.Text('Avaliação 3 >>', size=(11, 0)), Sg.Text('', size=(5, 0), key='-n3-'),
         Sg.Text('Avaliação 4 >>', size=(11, 0)), Sg.Text('', size=(5, 0), key='-n4-')],
        [Sg.Text('Disciplina >>', size=(11, 0)), Sg.Text('', size=(37, 0), key='-dip-')],
        [Sg.Output(size=(85, 27), key='-out-')],
        [Sg.Button('Tela menu(<)', size=(18, 0))]
    ]
    window = Sg.Window('RELATÓRIO', layout3, size=(735, 630))
    while True:
        event20, value20 = window.read()
        if event20 == 'Tela menu(<)' or event20 == Sg.WIN_CLOSED:
            break
        dado3 = []
        if event20 == 'Relatório':
            dado2 = mediauni.bduni.atuliz()
            vari = value20['-comb-']
            if vari:
                if vari in dado2:
                    dado1 = mediauni.bduni.lertab0(vari)
                    for d in dado1:
                        for v in d:
                            dado3.append(v)
                    window.find_element('-out-').Update('')
                    medf = mediauni.bduni.media_final(dado3[1], dado3[2], dado3[3], dado3[4])
                    mediauni.bduni.med_estat(dado3[0], dado3[1], dado3[2], dado3[3], dado3[4])
                    mediauni.bduni.peso(dado3[1], dado3[2], dado3[3], dado3[4])
                    mediauni.bduni.infprova(dado3[1], dado3[2], dado3[3], dado3[4])
                    mediauni.bduni.med_final(dado3[1], dado3[2], dado3[3], dado3[4])
                    mediauni.bduni.situacao(dado3[1], dado3[2], dado3[3], dado3[4])
                    window.find_element('-dip-').Update(dado3[0].capitalize())
                    window.find_element('-n1-').Update(dado3[1])
                    window.find_element('-n2-').Update(dado3[2])
                    window.find_element('-n3-').Update(dado3[3])
                    window.find_element('-n4-').Update(dado3[4])
                    window.find_element('-mf-').Update(medf)
                    mediauni.bduni.up(window, '-comb-')
                else:
                    window.find_element('-out-').Update('')
                    window.find_element('-comb-').Update('')
                    Sg.popup_auto_close('ERRO! "Disciplina" inexistente no banco de dados')
            else:
                window.find_element('-out-').Update('')
                Sg.popup_auto_close('ERRO! Selecione uma "Disciplina"')
    window.close()


janela_inicio()
