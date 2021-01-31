import sqlite3
import PySimpleGUI as Sg


def criar():
    media = sqlite3.connect('media.db')
    c = media.cursor()
    media.execute('''CREATE TABLE IF NOT EXISTS media(
                  DISCIPLINA TEXT PRIMARY KEY NOT NULL , 
                  NOTA1 REAL NOT NULL ,
                  NOTA2 REAL NOT NULL ,
                  NOTA3 REAL NOT NULL ,
                  NOTA4 REAL NOT NULL )''')
    media.commit()
    c.close()
    media.close()


def escrever(disciplina, nota1=0, nota2=0, nota3=0, nota4=0):
    try:
        media4 = sqlite3.connect('media.db')
        cur = media4.cursor()
        cur.execute('''INSERT into media(disciplina, nota1, nota2, nota3, nota4) VALUES (?, ?, ?, ?, ?)''',
                    (disciplina, nota1, nota2, nota3, nota4))
        media4.commit()
    except sqlite3.Error as erro:
        print(erro)
    else:
        cur.close()
        media4.close()


def alterar1(nota1, disciplina):
    try:
        media6 = sqlite3.connect('media.db')
        cursorr = media6.cursor()
        cursorr.execute('''UPDATE  media SET nota1 = ? WHERE disciplina = ?''',
                        (nota1, disciplina))
        media6.commit()
    except sqlite3.Error as erro:
        print(erro)
    else:
        cursorr.close()
        media6.close()


def alterar2(nota2, disciplina):
    try:
        media7 = sqlite3.connect('media.db')
        cursorr = media7.cursor()
        cursorr.execute('''UPDATE  media SET nota2 = ? WHERE disciplina = ?''',
                        (nota2, disciplina))
        media7.commit()
    except sqlite3.Error as erro:
        print(erro)
    else:
        cursorr.close()
        media7.close()


def alterar3(nota3, disciplina):
    try:
        media8 = sqlite3.connect('media.db')
        cursorr = media8.cursor()
        cursorr.execute('''UPDATE  media SET nota3 = ? WHERE disciplina = ?''',
                        (nota3, disciplina))
        media8.commit()
    except sqlite3.Error as erro:
        print(erro)
    else:
        cursorr.close()
        media8.close()


def alterar4(nota4, disciplina):
    try:
        media9 = sqlite3.connect('media.db')
        cursorr = media9.cursor()
        cursorr.execute('''UPDATE  media SET nota4 = ? WHERE disciplina = ?''',
                        (nota4, disciplina))
        media9.commit()
    except sqlite3.Error as erro:
        print(erro)
    else:
        cursorr.close()
        media9.close()


def delete(disciplina):
    try:
        media10 = sqlite3.connect('media.db')
        cursa = media10.cursor()
        cursa.execute('''DELETE FROM media WHERE disciplina = ?; ''',
                      (disciplina,))
        media10.commit()
    except sqlite3.Error as erro:
        print(erro)
    else:
        cursa.close()
        media10.close()


def lertab():
    try:
        media5 = sqlite3.connect('media.db')
        cursi = media5.cursor()
        sql_select_query = '''SELECT * FROM media'''
        cursi.execute(sql_select_query)
        records = cursi.fetchall()
    except sqlite3.Error as erro:
        print(erro)
    else:
        cursi.close()
        media5.close()
        return records


def lertab0(ide):
    try:
        media1 = sqlite3.connect('media.db')
        cursor = media1.cursor()
        sql_select_query = """select * from media where DISCIPLINA = ?"""
        cursor.execute(sql_select_query, (ide,))
        records = cursor.fetchall()
    except sqlite3.Error as erro:
        print(erro)
    else:
        cursor.close()
        media1.close()
        return records


def up(*lst):
    arg = lst[0]
    for i in range((len(lst) - 1), 0, -1):
        arg.find_element(lst[i]).Update('')


def med_estat(dis='', not1=0, not2=0, not3=0, not4=0):
    mediamom = ((not1 * 1.5 / 10) + (not2 * 1.5 / 10) + (not3 * 3.0 / 10) + (not4 * 4.0 / 10))
    media6 = media9 = 6.52
    media7 = 7.0
    media8 = 10
    if 10 >= not1 >= 0 and 10 >= not2 >= 0 and 10 >= not3 >= 0 and 10 >= not4 >= 0:
        linha23()
        print('Disciplina >>> {}'.format(dis))
        linha23()
        print(f'{"MÉDIA / FALTAS / SOBRAS (PONTOS):":<50}')
        print()
        print(f'Média conquistada   =   {mediamom:.2f}')
        if 10 >= not1 >= 0 and 10 >= not2 >= 0 and 10 >= not3 >= 0 and 10 >= not4 >= 0:
            if mediamom < media7:
                print(f'Falta para atingir a média 7,0   =   {media7 - mediamom:.2f}')
            elif mediamom == media7:
                print(f'Não houve sobras nem faltas em relação à média 7,0   =   {mediamom - media7:.2f}')
            else:
                print(f'Você já atingiu a média 7,0 e ultrapassou   =   {mediamom - media7:.2f}')
        if 10 >= not1 >= 0 and 10 >= not2 >= 0 and 10 >= not3 >= 0 and 10 >= not4 >= 0:
            if mediamom < media6:
                print(f'Falta para atingir a media 6,52 para arredondamento   =   {media6 - mediamom:.2f}')
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
        if 10 >= not1 >= 0 and 10 >= not2 >= 0 and 10 >= not3 >= 0 and 10 >= not4 >= 0:
            print(f'{"FALTA / SOBRAS (PERCENTUAIS):":<50}')
            print()
            print(f'Percentual faltante em relação ao curso   =   {(media8 - mediamom) * 100 / 10:.1f} %')
        if 10 >= not1 >= 0 and 10 >= not2 >= 0 and 10 >= not3 >= 0 and 10 >= not4 >= 0:
            if (media7 - mediamom) * 100 / media7 > 0:
                print(f'Percentual faltante em relação à média 7,0   =   '
                      f'{(media7 - mediamom) * 100 / media7:.1f} %')
            elif (media7 - mediamom) * 100 / media7 == 0:
                print(f'Não houve faltas ou sobras em relação à média 7,0   =   '
                      f'{(media7 - mediamom) * 100 / media7:.1f} %')
            else:
                print(f'Você ultrapassou a média 7,0 em   =   '
                      f'{(media7 - mediamom) * 100 / media7 - (media7 - mediamom) * 100 / media7 * 2:.1f} %')
        if 10 >= not1 >= 0 and 10 >= not2 >= 0 and 10 >= not3 >= 0 and 10 >= not4 >= 0:
            if (media9 - mediamom) * 100 / media6 > 0:
                print(f'Percentual faltante em relação à média 6,52 (Para arredondamento)   =   '
                      f'{(media9 - mediamom) * 100 / media6:.1f} %')
            elif (media9 - mediamom) * 100 / media6 == 0:
                print(f'Não houve faltas ou sobras em relação à média 6,52 (Para arredondamento)   =   '
                      f'{(media9 - mediamom) * 100 / media6:.1f} %')
            else:
                print(f'Você ultrapassou a média 6,52 (Para arredondamento) em   =   '
                      f'{(media9 - mediamom) * 100 / media6 - (media9 - mediamom) * 100 / media6 * 2:.1f} %')
        print()
        linha23()
    else:
        print('ERRO-As notas informadas não geram uma média válida! Verifique')
        print()
        linha23()


def linha22(arg):
    linhas = Sg.Text('____' * arg)
    return linhas


def linha23():
    linhas = '-' * 135
    print(linhas)


def peso(not1=0, not2=0, not3=0, not4=0):
    media1 = not1 * 1.5 / 10
    media2 = not2 * 1.5 / 10
    media3 = not3 * 3.0 / 10
    media4 = not4 * 4.0 / 10
    mediamom = (media1 + media2 + media3 + media4)
    print()
    print(f'{"PESO DE CADA PROVA NA MÉDIA FINAL OBTIDA:":<50}')
    if mediamom > 0:
        print()
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
        print()
        print(f'Cálculo indisponível, pois a média tem valor = 0!')
        print()
        linha23()


def infprova(n1=0, n2=0, n3=0, n4=0):
    mediamom = ((n1 * 1.5 / 10) + (n2 * 1.5 / 10) + (n3 * 3.0 / 10) + (n4 * 4.0 / 10))
    for u in range(1, 5):
        if u == 1:
            media1 = n1 * 1.5 / 10
            print(f'INFORMAÇÕES REFERENTE À PROVA 01:')
            print()
            print(f'Nota   obtida na prova 01 =  {n1:.2f}')
            print(f'Média obtida na prova 01 =  {media1:.2f}')
            if mediamom > 0:
                print(f'Peso da prova 01 na média (pontos percentuais)   =   {media1 * 100 / mediamom:.1f} %')
            else:
                print(f'Cálculo do peso da prova 01 indisponível, pois a média tem valor = 0!')
            print()
        if u == 2:
            media2 = n2 * 1.5 / 10
            print(f'INFORMAÇÕES REFERENTE À PROVA 02:')
            print()
            print(f'Nota   obtida na prova 02 =  {n2:.2f}')
            print(f'Média obtida na prova 02 =  {media2:.2f}')
            if mediamom > 0:
                print(f'Peso da prova 02 na média (pontos percentuais)   =   {media2 * 100 / mediamom:.1f} %')
            else:
                print(f'Cálculo do peso da prova 02 indisponível, pois a média tem valor = 0!')
            print()
        if u == 3:
            media3 = n3 * 3.0 / 10
            print(f'INFORMAÇÕES REFERENTE À PROVA 03:')
            print()
            print(f'Nota   obtida na prova 03 =  {n3:.2f}')
            print(f'Média obtida na prova 03 =  {media3:.2f}')
            if mediamom > 0:
                print(f'Peso da prova 03 na média (pontos percentuais)   =   {media3 * 100 / mediamom:.1f} %')
            else:
                print(f'Cálculo do peso da prova 03 indisponível, pois a média tem valor = 0!')
            print()
        if u == 4:
            media4 = n4 * 4.0 / 10
            print(f'INFORMAÇÕES REFERENTE À PROVA 04:')
            print()
            print(f'Nota   obtida na prova 04 =  {n4:.2f}')
            print(f'Média obtida na prova 04 =  {media4:.2f}')
            if mediamom > 0:
                print(f'Peso da prova 04 na média (pontos percentuais)   =   {media4 * 100 / mediamom:.1f} %')
            else:
                print(f'Cálculo do peso da prova 04 indisponível, pois a média tem valor = 0!')
            print()
        linha23()


def med_final(n1=0, n2=0, n3=0, n4=0):
    mediamom = ((n1 * 1.5 / 10) + (n2 * 1.5 / 10) + (n3 * 3.0 / 10) + (n4 * 4.0 / 10))
    print(f'{"SUA MÉDIA FINAL: ":<50}')
    print()
    if n1 == 0 and n2 > 0 and n3 > 0 and n4 > 0:
        print(f'Sua média final foi (Prova 01 não obteve pontos > 0)   =   {mediamom:.2f}')
        print()
        linha23()
    elif n1 > 0 and n2 == 0 and n3 > 0 and n4 > 0:
        print(f'Sua média final foi (Prova 02 não obteve pontos > 0)   =   {mediamom:.2f}')
        print()
        linha23()
    elif n1 > 0 and n2 > 0 and n3 == 0 and n4 > 0:
        print(f'Sua média final foi (Prova 03 não obteve pontos > 0)   =   {mediamom:.2f}')
        print()
        linha23()
    elif n1 > 0 and n2 > 0 and n3 > 0 and n4 == 0:
        print(f'Sua média final foi (Prova 04 não obteve pontos > 0)   =   {mediamom:.2f}')
        print()
        linha23()
    elif n1 > 0 and n2 > 0 and n3 > 0 and n4 > 0:
        print(f'Sua média final foi (Todas as provas possuem valor > 0)   =   {mediamom:.2f}')
        print()
        linha23()
    else:
        print(f'Média final não disponível, pois mais de uma prova esta com valor = 0!')
        print()
        linha23()


def situacao(n1=0, n2=0, n3=0, n4=0):
    mediamom = ((n1 * 1.5 / 10) + (n2 * 1.5 / 10) + (n3 * 3.0 / 10) + (n4 * 4.0 / 10))
    media7 = 7.0
    media6 = 6.52
    print(f'{"SITUAÇÃO: ":<50}')
    print()
    if (n1 == 0 and n2 > 0 and n3 > 0 and n4 > 0 or
            n1 > 0 and n2 == 0 and n3 > 0 and n4 > 0 or
            n1 > 0 and n2 > 0 and n3 == 0 and n4 > 0 or
            n1 > 0 and n2 > 0 and n3 > 0 and n4 == 0 or
            n1 > 0 and n2 > 0 and n3 > 0 and n4 > 0):
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
        print(f'Não é possível verificar sua situação, pois mais de uma prova esta com valor = 0!')
        print()
        linha23()


def media_final(n1=0, n2=0, n3=0, n4=0):
    m1 = n1 * 1.50 / 10
    m2 = n2 * 1.50 / 10
    m3 = n3 * 3.00 / 10
    m4 = n4 * 4.00 / 10
    mf = (m1 + m2 + m3 + m4)
    return f'{mf:.2f}'


def aproveitamento(*args):
    not10 = 10
    ger = maio = meno = cont = 0
    nomma = ''
    nomme = ''
    try:
        for t in args:
            print()
            for m in t:
                m1 = m[1] * 1.50 / 10
                m2 = m[2] * 1.50 / 10
                m3 = m[3] * 3.00 / 10
                m4 = m[4] * 4.00 / 10
                mf = (m1 + m2 + m3 + m4)
                porc = mf * 100 / not10
                mat = m[0]
                if porc > 0:
                    ger += porc
                    cont += 1
                print(f'Disciplina: ', end='')
                print(f'{mat}'.capitalize())
                print(f'Aproveitamento = {porc:.1f}%')
                if m == t[0]:
                    nomma = mat
                    nomme = mat
                    maio = porc
                    meno = porc
                if porc > maio:
                    maio = porc
                    nomma = mat
                if porc < meno and porc != 0:
                    meno = porc
                    nomme = mat
                if m != t[-1]:
                    linha23()
        ger1 = ger / cont
    except(ValueError, TypeError, IndexError, ZeroDivisionError):
        print('Algo deu errado')
    else:
        return ger1, nomma, maio, nomme, meno


def janela_final():
    layout13 = [
        [Sg.Text('ATÉ BREVE!')],
        [Sg.Text('OBRIGADO VOLTE SEMPRE!')],
        [Sg.Button('Sair(x)', size=(11, 0))]
    ]
    final = Sg.Window('CÁLCULO MÉDIA v2.0', layout13, size=(400, 97), element_justification='center')
    event, value = final.read()
    if event == 'Sair(x)' or event == Sg.WIN_CLOSED:
        final.close()


def atuliz():
    dado = lertab()
    dado2 = []
    for v in dado:
        dado2.append(v[0])
    return dado2


def atuliz0():
    dado = lertab()
    return dado


def aluliz1(arg):
    dado3 = []
    dado1 = lertab0(arg)
    for d in dado1:
        for v in d:
            dado3.append(v)
    return dado3


def janela_delete():
    layout55 = [
        [Sg.Text('Linha de dados excluída com sucesso!')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    delete1 = Sg.Window('ERRO', layout55, size=(450, 97), element_justification='center')
    event3, value3 = delete1.read()
    if event3 == 'OK' or event3 == Sg.WIN_CLOSED:
        delete1.close()


def janela_erro8():
    layout51 = [
        [Sg.Text('ERRO! Selecione uma disciplina para alterar os dados.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    erro8 = Sg.Window('ERRO', layout51, size=(450, 97), element_justification='center')
    event4, value4 = erro8.read()
    if event4 == 'OK' or event4 == Sg.WIN_CLOSED:
        erro8.close()


def janela_erro7():
    layout57 = [
        [Sg.Text('ERRO! Selecione uma disciplina para exclusão.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    erro7 = Sg.Window('ERRO', layout57, size=(450, 97), element_justification='center')
    event5, value5 = erro7.read()
    if event5 == 'OK' or event5 == Sg.WIN_CLOSED:
        erro7.close()


def janela_erro6():
    layout58 = [
        [Sg.Text('ERRO! Disciplina inexistente no banco de dados.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    erro6 = Sg.Window('ERRO', layout58, size=(450, 97), element_justification='center')
    event6, value6 = erro6.read()
    if event6 == 'OK' or event6 == Sg.WIN_CLOSED:
        erro6.close()


def janela_erro5():
    layout84 = [
        [Sg.Text('ERRO! Os campos de alteração só podem conter números.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    erro5 = Sg.Window('ERRO', layout84, size=(450, 97), element_justification='center')
    event7, value7 = erro5.read()
    if event7 == 'OK' or event7 == Sg.WIN_CLOSED:
        erro5.close()


def janela_erro4():
    layout88 = [
        [Sg.Text('ERRO! Selecione uma disciplina para carregar os dados.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    erro4 = Sg.Window('ERRO', layout88, size=(450, 97), element_justification='center')
    event8, value8 = erro4.read()
    if event8 == 'OK' or event8 == Sg.WIN_CLOSED:
        erro4.close()


def janela_erro3():
    layout89 = [
        [Sg.Text('ERRO! Disciplina inexistente no banco de dados.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    erro3 = Sg.Window('ERRO', layout89, size=(450, 97), element_justification='center')
    event9, value9 = erro3.read()
    if event9 == 'OK' or event9 == Sg.WIN_CLOSED:
        erro3.close()


def janela_erro2():
    layout95 = [
        [Sg.Text('ERRO! Selecione uma "Disciplina.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    erro2 = Sg.Window('ERRO', layout95, size=(450, 97), element_justification='center')
    event10, value10 = erro2.read()
    if event10 == 'OK' or event10 == Sg.WIN_CLOSED:
        erro2.close()


def janela_nots():
    layout96 = [
        [Sg.Text('ERRO! Uma ou mais notas é > 10 ou < 0.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    nots = Sg.Window('ERRO', layout96, size=(450, 97), element_justification='center')
    event11, value11 = nots.read()
    if event11 == 'OK' or event11 == Sg.WIN_CLOSED:
        nots.close()


def janela_disc():
    layout97 = [
        [Sg.Text('ERRO! O campo "DISCIPLINA" não pode ser vazio.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    disc = Sg.Window('ERRO', layout97, size=(450, 97), element_justification='center')
    event12, value12 = disc.read()
    if event12 == 'OK' or event12 == Sg.WIN_CLOSED:
        disc.close()


def janela_ok():
    layout98 = [
        [Sg.Text('OK! Informações inseridas no banco de dados com sucesso.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    ok = Sg.Window('OK', layout98, size=(450, 97), element_justification='center')
    event13, value13 = ok.read()
    if event13 == 'OK' or event13 == Sg.WIN_CLOSED:
        ok.close()


def janela_errobanco():
    layout99 = [
        [Sg.Text('ERRO! Erro ao inserir informações no banco de dados.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    errobanco = Sg.Window('ERRO', layout99, size=(450, 97), element_justification='center')
    event14, value14 = errobanco.read()
    if event14 == 'OK' or event14 == Sg.WIN_CLOSED:
        errobanco.close()


def janela_erro1():
    layout0 = [
        [Sg.Text('ERRO! Os campos "AVALIAÇÃO" só podem conter números.')],
        [Sg.Button('OK', size=(12, 0))]
    ]
    erro = Sg.Window('ERRO', layout0, size=(450, 97), element_justification='center')
    event15, value15 = erro.read()
    if event15 == 'OK' or event15 == Sg.WIN_CLOSED:
        erro.close()
