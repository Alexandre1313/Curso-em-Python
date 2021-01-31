import PySimpleGUI as Sg


class TelaPython:
    def __init__(self):
        # layout
        self.values = None
        self.button = None
        Sg.theme('DarkPurple4')
        layout = [
            [Sg.Text('Nota 01', size=(9, 0)), Sg.Input('0', size=(5, 0)), Sg.Button('Obter informações da prova 01'),
             Sg.Button('Nota mínima na prova 01')],
            [Sg.Text('Nota 02', size=(9, 0)), Sg.Input('0', size=(5, 0)), Sg.Button('Obter informações da prova 02'),
             Sg.Button('Nota mínima na prova 02')],
            [Sg.Text('Nota 03', size=(9, 0)), Sg.Input('0', size=(5, 0)), Sg.Button('Obter informações da prova 03'),
             Sg.Button('Nota mínima na prova 03')],
            [Sg.Text('Nota 04', size=(9, 0)), Sg.Input('0', size=(5, 0)), Sg.Button('Obter informações da prova 04'),
             Sg.Button('Nota mínima na prova 04')],
            [Sg.Button('Gerar estatísticas'), Sg.Button('Fechar')],
            [Sg.Output(size=(100, 25))]
        ]
        # Janela
        self.janela = Sg.Window('CÁLCULO MÉDIA UNIASSELVI v1.0', size=(900, 600)).Layout(layout)

    def iniciar(self):
        while True:
            # Extrair os dados da tela
            [self.button, self.values] = self.janela.Read()
            botao = self.button  # Variável que recebe o valor de determinado botão da janela
            if botao == 'Fechar':
                exit()
                break
            # Abaixo lista recebendo valores vindos da janela e convertendo de string para ponto flutuante:
            lista = [float(self.values[0]), float(self.values[1]), float(self.values[2]), float(self.values[3])]
            media7 = 7.0  # Constante contendo a média para comparação, média (7,0)
            media8 = 10  # Constante contendo a média de comparação, média (10)
            # Abaixo constante contendo a média para comparação, média (6,52), media de arredondamento
            media6 = media9 = 6.52
            media1 = lista[0] * 1.5 / 10  # Calcula média da prova 01
            media2 = lista[1] * 1.5 / 10  # Calcula média da prova 02
            media3 = lista[2] * 3.0 / 10  # Calcula média da prova 03
            media4 = lista[3] * 4.0 / 10  # Calcula média da prova 04
            mediamom = (media1 + media2 + media3 + media4)  # Soma todas as médias
            if botao == 'Obter informações da prova 01':
                if 10 >= lista[0] >= 0:
                    print(f'{"INFORMAÇÕES REFERENTE À PROVA 01:":<50}')
                    print()
                    print(f'Nota   obtida na prova 01 =  {lista[0]:.1f}')
                    print(f'Média obtida na prova 01 =  {media1:.1f}')
                    print()
                else:
                    print(f'ERRO-A nota informada, no caso a nota  {lista[0]}  não é válida! Verifique')
                    print()
            if botao == 'Obter informações da prova 02':
                if 10 >= lista[1] >= 0:
                    print(f'{"INFORMAÇÕES REFERENTE À PROVA 02:":<50}')
                    print()
                    print(f'Nota   obtida na prova 02 =  {lista[1]:.1f}')
                    print(f'Média obtida na prova 02 =  {media2:.1f}')
                    print()
                else:
                    print(f'ERRO-A nota informada, no caso a nota  {lista[1]}  não é válida! Verifique')
                    print()
            if botao == 'Obter informações da prova 03':
                if 10 >= lista[2] >= 0:
                    print(f'{"INFORMAÇÕES REFERENTE À PROVA 03:":<50}')
                    print()
                    print(f'Nota   obtida na prova 03 =  {lista[2]:.1f}')
                    print(f'Média obtida na prova 03 =  {media3:.1f}')
                    print()
                else:
                    print(f'ERRO-A nota informada, no caso a nota  {lista[2]}  não é válida! Verifique')
                    print('-' * 97)
            if botao == 'Obter informações da prova 04':
                if 10 >= lista[3] >= 0:
                    print(f'{"INFORMAÇÕES REFERENTE À PROVA 04:":<50}')
                    print()
                    print(f'Nota   obtida na prova 04 =  {lista[3]:.1f}')
                    print(f'Média obtida na prova 04 =  {media4:.1f}')
                    print()
                else:
                    print(f'ERRO-A nota informada, no caso a nota  {lista[3]}  não é válida! Verifique')
                    print()
            if botao == 'Gerar estatísticas':
                if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                    print(f'{"MÉDIA / FALTAS / SOBRAS (PONTOS):":<50}')
                    print()
                    print(f'Média conquistada   =   {mediamom:.3f}')
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        if mediamom < media7:
                            print(f'Falta para atingir a média 7,0   =   {media7 - mediamom:.3f}')
                        elif mediamom == media7:
                            print(f'Não houve sobras nem faltas em relação à média 7,0   =   {mediamom - media7:.3f}')
                        else:
                            print(f'Você já atingiu a média 7,0 e ultrapassou   =   {mediamom - media7:.3f}')
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        if mediamom < media6:
                            print(f'Falta para atingir a media 6,52 para arredondamento   =   {media6 - mediamom:.3f}')
                        elif mediamom == media6:
                            print(f'Não houve sobras nem faltas em relação à média 6,52 para arredondamento   '
                                  f'=   {mediamom - media6:.3f}')
                        else:
                            print(f'Você já atingiu a média 6,52 para arredondamento e ultrapassou   '
                                  f'=   {mediamom - media6:.3f}')
                    print()
                    print(f'{"PERCENTUAIS JÁ CONQUISTADOS:":<50}')
                    print()
                    print(f'Percentual já atingido em relação ao curso   =   {mediamom * 100 / 10:.1f} %')
                    print(f'Percentual já atingido em relação à média 7,0   =   {mediamom * 100 / media7:.1f} %')
                    print(f'Percentual já atingido em relação à média 6,52 (para '
                          f'arredondamento)   =   {mediamom * 100 / media6:.1f} %')
                    print()
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        print(f'{" FALTA / SOBRAS (PERCENTUAIS):":<50}')
                        print()
                        print(f'Percentual faltante em relação ao curso   =   {(media8 - mediamom) * 100 / 10:.1f} %')
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        if (media7 - mediamom) * 100 / media7 > 0:
                            print(f'Percentual faltante em relação à média 7,0   =   '
                                  f'{(media7 - mediamom) * 100 / media7:.1f} %')
                        elif (media7 - mediamom) * 100 / media7 == 0:
                            print(f'Não houve faltas ou sobras em relação à média 7,0   =   '
                                  f'{(media7 - mediamom) * 100 / media7:.1f} %')
                        else:
                            print(f'Você ultrapassou a média 7,0 em   =   '
                                  f'{(media7 - mediamom) * 100 / media7-(media7 - mediamom) * 100 / media7 * 2:.1f} %')
                    if 10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0:
                        if (media9 - mediamom) * 100 / media6 > 0:
                            print(f'Percentual faltante em relação à média 6,52 (Para arredondamento)   =   '
                                  f'{(media9 - mediamom) * 100 / media6:.1f} %')
                        elif (media9 - mediamom) * 100 / media6 == 0:
                            print(f'Não houve faltas ou sobras em relação à média 6,52 (Para arredondamento)   =   '
                                  f'{(media9 - mediamom) * 100 / media6:.1f} %')
                        else:
                            print(f'Você ultrapassou a média 6,52 (Para arredondamento) em   =   '
                                  f'{(media9 - mediamom) * 100 / media6-(media9 - mediamom) * 100 / media6 * 2:.1f} %')
                    print()
                else:
                    print('ERRO-As notas informadas não geram uma média válida! Verifique')
                    print()
            if botao == 'Nota mínima na prova 01':
                if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                        and lista[0] == 0):
                    print(f'{" NOTA PENDENTE PROVA 01 (PARA APROVAÇÃO COM MÉDIA 7,0):":<50}')
                    print()
                    var7 = (media7 - mediamom) * 10 / 1.5
                    if 10 >= var7 >= 0:
                        print(f'Para aprovação com média 7,0 você precisa tirar   =   {var7:.3f}')
                    elif var7 > 10:
                        print(f'Já não há o que fazer, tente a nota por arredondamento')
                    else:
                        print(f'Nota não necessária para aprovação ==> JÁ APROVADO')
                    print()
                if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                        and lista[0] == 0):
                    print(f'{" NOTA PENDENTE PROVA 01 (PARA APROVAÇÃO COM MÉDIA 6,52 (ARREDONDAMENTO)):":<50}')
                    print()
                    var6 = (media6 - mediamom) * 10 / 1.5
                    if 10 >= var6 >= 0:
                        print(f'Para aprovação com média 6,52 (Para arredondamento) '
                              f'você precisa tirar   =   {var6:.3f}')
                    elif var6 > 10:
                        print(f'Já não há o que fazer, pois necessitaria de um   =   {var6:.3f}')
                    else:
                        print('Nota não necessária para aprovação ==> JÁ APROVADO')
                    print()
                else:
                    print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 01 '
                          f'é diferente de 0 ! Verifique')
                    print()
            if botao == 'Nota mínima na prova 02':
                if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                        and lista[1] == 0):
                    print(f'{" NOTA PENDENTE PROVA 02 (PARA APROVAÇÃO COM MÉDIA 7,0):":<50}')
                    print()
                    var7 = (media7 - mediamom) * 10 / 1.5
                    if 10 >= var7 >= 0:
                        print(f'Para aprovação com média 7,0 você precisa tirar   =   {var7:.3f}')
                    elif var7 > 10:
                        print(f'Já não há o que fazer, tente a nota por arredondamento')
                    else:
                        print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 02 '
                              f'é diferente de 0 ! Verifique')
                    print()
                if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                        and lista[1] == 0):
                    print(f'{" NOTA PENDENTE PROVA 02 (PARA APROVAÇÃO COM MÉDIA 6,52 (ARREDONDAMENTO)):":<50}')
                    print()
                    var6 = (media6 - mediamom) * 10 / 1.5
                    if 10 >= var6 >= 0:
                        print(f'Para aprovação com média 6,52 (Para arredondamento) '
                              f'você precisa tirar   =   {var6:.3f}')
                    elif var6 > 10:
                        print(f'Já não há o que fazer, pois necessitaria de um   =   {var6:.3f}')
                    else:
                        print('Nota não necessária para aprovação ==> JÁ APROVADO')
                    print()
                else:
                    print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 02 '
                          f'é diferente de 0 ! Verifique')
                    print()
            if botao == 'Nota mínima na prova 03':
                if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                        and lista[2] == 0):
                    print(f'{" NOTA PENDENTE PROVA 03 (PARA APROVAÇÃO COM MÉDIA 7,0):":<50}')
                    print()
                    var7 = (media7 - mediamom) * 10 / 3.0
                    if 10 >= var7 >= 0:
                        print(f'Para aprovação com média 7,0 você precisa tirar   =   {var7:.3f}')
                    elif var7 > 10:
                        print(f'Já não há o que fazer, tente a nota por arredondamento')
                    else:
                        print(f'Nota não necessária para aprovação ==> JÁ APROVADO')
                    print()
                if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                        and lista[2] == 0):
                    print(f'{" NOTA PENDENTE PROVA 03 (PARA APROVAÇÃO COM MÉDIA 6,52 (ARREDONDAMENTO)):":<50}')
                    print()
                    var6 = (media6 - mediamom) * 10 / 3.0
                    if 10 >= var6 >= 0:
                        print(f'Para aprovação com média 6,52 (Para arredondamento) '
                              f'você precisa tirar   =   {var6:.3f}')
                    elif var6 > 10:
                        print(f'Já não há o que fazer, pois necessitaria de um   =   {var6:.3f}')
                    else:
                        print('Nota não necessária para aprovação ==> JÁ APROVADO')
                    print()
                else:
                    print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 03 '
                          f'é diferente de 0 ! Verifique')
                    print()
            if botao == 'Nota mínima na prova 04':
                if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                        and lista[3] == 0):
                    print(f'{" NOTA PENDENTE PROVA 04 (PARA APROVAÇÃO COM MÉDIA 7,0):":<50}')
                    print()
                    var7 = (media7 - mediamom) * 10 / 4.0
                    if 10 >= var7 >= 0:
                        print(f'Para aprovação com média 7,0 você precisa tirar   =   {var7:.3f}')
                    elif var7 > 10:
                        print(f'Já não há o que fazer, tente a nota por arredondamento')
                    else:
                        print(f'Nota não necessária para aprovação ==> JÁ APROVADO')
                    print()
                if (10 >= lista[0] >= 0 and 10 >= lista[1] >= 0 and 10 >= lista[2] >= 0 and 10 >= lista[3] >= 0
                        and lista[3] == 0):
                    print(f'{" NOTA PENDENTE PROVA 04 (PARA APROVAÇÃO COM MÉDIA 6,52 (ARREDONDAMENTO)):":<50}')
                    print()
                    var6 = (media6 - mediamom) * 10 / 4.0
                    if 10 >= var6 >= 0:
                        print(f'Para aprovação com média 6,52 (Para arredondamento) '
                              f'você precisa tirar   =   {var6:.3f}')
                    elif var6 > 10:
                        print(f'Já não há o que fazer, pois necessitaria de um   =   {var6:.3f}')
                    else:
                        print('Nota não necessária para aprovação ==> JÁ APROVADO')
                    print()
                else:
                    print(f'ERRO-As notas informadas não geram uma média válida, ou a nota da prova 04 '
                          f'é diferente de 0 ! Verifique')
                    print()


tela = TelaPython()
tela.iniciar()
