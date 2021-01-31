import PySimpleGUI as Sg


class tela_python:
    def __init__(self):
        # layout
        self.dados = None
        self.button = None
        Sg.theme('DarkTeal10')
        # Sg.preview_all_look_and_feel_themes()
        layout = [
            [Sg.Text('Nota 01', size=(9, 0)), Sg.Input('0', size=(5, 0)), Sg.Button('Calcular média 01')],
            [Sg.Text('Nota 02', size=(9, 0)), Sg.Input('0', size=(5, 0)), Sg.Button('Calcular média 02')],
            [Sg.Text('Nota 03', size=(9, 0)), Sg.Input('0', size=(5, 0)), Sg.Button('Calcular média 03')],
            [Sg.Text('Nota 04', size=(9, 0)), Sg.Input('0', size=(5, 0)), Sg.Button('Calcular média 04')],
            [Sg.Button('Gerar estatísticas'), Sg.Button('Sair'), Sg.Button('Fechar')],
            [Sg.Output(size=(100, 25))]
            ]
        # Janela
        self.janela = Sg.Window('CÁLCULO MÉDIA UNIASSELVI v1.0', size=(900, 600)).Layout(layout)

    def iniciar(self):
        try:
            while True:
                # Extrair os dados da tela
                [self.button, self.dados] = self.janela.Read()
                # Abaixo lista recebendo valores vindos da janela e convertendo de string para ponto flutuante:
                lista = [float(self.dados[0]), float(self.dados[1]), float(self.dados[2]), float(self.dados[3])]
                botao = self.button  # Variável que recebe o valor de determinado botão da janela
                media7 = media8 = 7.0  # Constante contendo a média para comparação, média (7,0)
                # Abaixo constante contendo a média para comparação, média (6,52), media de arredondamento
                media6 = media9 = 6.52
                media1 = lista[0] * 1.5 / 10  # Calcula média da prova 01
                media2 = lista[1] * 1.5 / 10  # Calcula média da prova 02
                media3 = lista[2] * 3.0 / 10  # Calcula média da prova 03
                media4 = lista[3] * 4.0 / 10  # Calcula média da prova 04
                mediamom = (media1 + media2 + media3 + media4)  # Soma todas as médias
                if botao == 'Calcular média 01':
                    if 10 >= lista[0] >= 0:
                        print(f'{"INFORMAÇÕES REFERENTE À PROVA 01:":<50}')
                        print()
                        print(f'Nota   obtida na prova 01 =  {lista[0]:.1f}')
                        print(f'Média obtida na prova 01 =  {media1:.1f}')
                        print()
                    else:
                        print(f'ERRO-A nota informada, no caso a nota  {lista[0]}  não é válida! Verifique')
                        print()
                if botao == 'Calcular média 02':
                    if 10 >= lista[1] >= 0:
                        print(f'{"INFORMAÇÕES REFERENTE À PROVA 02:":<50}')
                        print()
                        print(f'Nota   obtida na prova 02 =  {lista[1]:.1f}')
                        print(f'Média obtida na prova 02 =  {media2:.1f}')
                        print()
                    else:
                        print(f'ERRO-A nota informada, no caso a nota  {lista[1]}  não é válida! Verifique')
                        print()
                if botao == 'Calcular média 03':
                    if 10 >= lista[2] >= 0:
                        print(f'{"INFORMAÇÕES REFERENTE À PROVA 03:":<50}')
                        print()
                        print(f'Nota   obtida na prova 03 =  {lista[2]:.1f}')
                        print(f'Média obtida na prova 03 =  {media3:.1f}')
                        print()
                    else:
                        print(f'ERRO-A nota informada, no caso a nota  {lista[2]}  não é válida! Verifique')
                        print('-' * 97)
                if botao == 'Calcular média 04':
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
                        print(f'{"MÉDIA / FALTAS:":<50}')
                        print()
                        print(f'Média conquistada   =   {mediamom:.3f}')
                        print(f'Falta para atingir a média 7,0   =   {media7 - mediamom:.3f}')
                        print(f'Falta para atingir a media por arredondamento   =   {media6 - mediamom:.3f}')
                        print()
                        print(f'{"PERCENTUAIS JÁ CONQUISTADOS:":<50}')
                        print()
                        print(f'Percentual já atingido em relação ao curso   =   {mediamom * 100 / 10:.1f} %')
                        print(f'Percentual já atingido em relação à média 7,0   =   {mediamom * 100 / media7:.1f} %')
                        print(f'Percentual já atingido em relação à média 6,52 (para '
                              f'arredondamento)   =   {mediamom * 100 / media6:.1f} %')
                        print()
                        print(f'{"PERCENTUAIS FALTANTES:":<50}')
                        print()
                        print(f'Percentual faltante em relação ao curso   =   {(media8 - mediamom) * 100 / 10:.1f} %')
                        print(f'Percentual faltante em relação à média 7,0   =   '
                              f'{(media8 - mediamom) * 100 / media7:.1f} %')
                        print(f'Percentual faltante em relação à média 6,52 (para '
                              f'arredondamento)   =   {(media9 - mediamom) * 100 / media6:.1f} %')
                        print()
                    else:
                        print('ERRO-As notas informadas não geram uma média válida! Verifique')
                        print()
                if botao == 'Sair':
                    break
        except(ValueError, TypeError):
            print(f'ERRO-A nota informada não é válida!')


tela = tela_python()
tela.iniciar()
