from tkinter import *


#  dicionário
#  width=
#  height=
#  background=


def janela_1():
    janela = Tk()  # Criação do objeto 'janela'

    # ---------------------------------------------------------------------------------------------------------------
    #  MANEIRA DE CALCULAR A LARGURA DE DETERMINADO MONITOR E CENTRALIZAR A TELA:
    largura = 750  # Primeiro define-se a largura que o objeto terá por padrao e se atribui à uma variável
    altura = 550  # Segundo define-se a altura que o objeto terá por padrão e se atribui à uma variável

    # AGORA OBTEREMOS ATRAVÉS DE MÉTODOS DO PRÓPRIO TEKINTER A RESULUÇÃO DO MONITOR:
    larg_monitor = janela.winfo_screenwidth()  # Esse método captará a largura do monitor
    alt_monitor = janela.winfo_screenheight()  # Esse método captará a altura do monitor e atribira a uma variavel

    # POSIÇÃO DO OBJETO (JANELA): FÓRMULA DE CÁLCULO
    posix = larg_monitor / 2 - largura / 2
    posiy = alt_monitor / 2 - altura / 2

    # DEFININDO A GEOMETRY: COM OS VALORES CALCULADOS ANTERIORMENTE
    janela.geometry("%dx%d+%d+%d" % (largura, altura, posix, posiy))

    # ---------------------------------------------------------------------------------------------------------------
    janela.title('Meu app')  # Modificando atributo 'título' do objeto 'janela'

    # ---------------------------------------------------------------------------------------------------------------
    janela.configure(background='black')  # Configurando a cor de fundo do objeto 'janela' através desse método

    # ---------------------------------------------------------------------------------------------------------------
    janela.resizable(True, True)  # Esse método dira se o objeto 'janela' sera ajustavel de tamanho, false não
    #  permite , se true a janela será redimensionável no sentido que for true

    # ---------------------------------------------------------------------------------------------------------------
    janela.minsize(width=750,
                   height=550)  # Esse método define o minimo tamanho que o objeto 'janela' pode atingir

    # ---------------------------------------------------------------------------------------------------------------
    #  janela.maxsize(width=900, height=700)  # Esse método estabelece o máximo tamanho que o objeto pode atingir
    #  oposto ao minsize()

    # ---------------------------------------------------------------------------------------------------------------
    #  janela.state('zoomed')  # Esse método inicializa o objeto maximizado, preenchendo a tela inteira
    #  seu oposto e só substituir 'zoomed' por 'iconic', neste último o objeto vai iciciar minimizado
    #  na barra de tarefas

    # ---------------------------------------------------------------------------------------------------------------
    janela.iconbitmap("Images icons/document_blank.ico")  # Esse método altera o icone na barra de titulo do objeto
    #  basta invocar o metodo e passar o endereço do icone, arquivo (.ico)

    # ---------------------------------------------------------------------------------------------------------------
    #  CRIAÇÃO DOS FRAMES, SÃO BLOCOS PARA DIVIDIR UMA JANELA
    frame_1 = Frame(janela,
                    bd=4,
                    bg='#dfe3ee',
                    highlightbackground='#759fe6',
                    highlightthickness=3,
                    relief='flat')
    frame_1.place(relx=0.007, rely=0.007, relwidth=0.986, relheight=0.4895)

    frame_2 = Frame(janela,
                    bd=4,
                    bg='#dfe3ee',
                    highlightbackground='#759fe6',
                    highlightthickness=3,
                    relief='flat')
    frame_2.place(relx=0.007, rely=0.5035, relwidth=0.986, relheight=0.4895)

    # ---------------------------------------------------------------------------------------------------------------
    #  CRIAÇÃO DOS BOTÕES, Á ELES SE ATRIBUI A EXECUÇÃO DE DETERMINADAS FUNÇÕES
    botao_1 = Button(frame_1,
                     bd=4,
                     bg='#dfe3ee',
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Executar')
    botao_1.place(relx=0.0007, rely=0.0007, relwidth=0.100, relheight=0.110)

    botao_2 = Button(frame_1,
                     bd=4,
                     relief='flat',
                     bg='#dfe3ee',
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Executar')
    botao_2.place(relx=0.1017, rely=0.0007, relwidth=0.100, relheight=0.110)

    botao_3 = Button(frame_1,
                     bd=4,
                     bg='#dfe3ee',
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Executar')
    botao_3.place(relx=0.2027, rely=0.0007, relwidth=0.100, relheight=0.110)

    botao_4 = Button(frame_1,
                     bd=4,
                     relief='flat',
                     bg='#dfe3ee',
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Executar')
    botao_4.place(relx=0.3037, rely=0.0007, relwidth=0.100, relheight=0.110)

    # ---------------------------------------------------------------------------------------------------------------
    #  CRIAÇÃO DOS LABEL, LABELS SÃO TEXTOS IMPRESSOS EM NOSSA JANELA, POR EXEMPLO INFORMAR ALGO
    label_1 = Label(frame_1,  # Define aonde determinado no caso label aparecera, nesse caso no frame 1
                    bd=1,  # Expessura de barda do elemento, para ter efeito tem de definir o relief
                    relief='raised',
                    bg='#ffaaee',  # Cor de fundo do elemento em hexadecimal precedido do simbolo #
                    highlightbackground='#759fe6',
                    highlightthickness=3,
                    text='Executar',  # Texto que será apresentado no label
                    font='Times',  # Fonte do texto, aqui se especifica tambem tamanho, italico, bold
                    fg='#759fe6',  # Cor do texto do label
                    anchor=CENTER,  # Posiciona o texto ao centro, seguindo a rosa dos ventos, por padrão é 'center'
                    padx=7,    # Define em pixel a distancia do texto da borda do label na horizontal
                    pady=7,    # Define em pixel a distancia do texto da borda do label na vertical
                    justify=LEFT)  # Justifica o texto a esquerda, direita ou centro
    label_1.place(relx=0.0007, rely=0.1207, relwidth=0.100, relheight=0.110)
    # ---------------------------------------------------------------------------------------------------------------
    label_2 = Label(frame_2,
                    bd=7,
                    relief='sunken',
                    bg='#ffaaee',
                    highlightbackground='#759fe6',
                    highlightthickness=3,
                    text='Alexandre',
                    font='Times 40',
                    anchor=CENTER,
                    padx=7,
                    pady=7,
                    justify=LEFT)
    label_2.place(relx=0.0007, rely=0.2407, relwidth=0.500, relheight=0.510)
    # ---------------------------------------------------------------------------------------------------------------
    janela.mainloop()  # Fazendo nosso objeto permanecer em loop através do método tkinter 'mainloop'


def root_principal():
    rp = Tk()
    texto = StringVar()
    largura = 750
    altura = 550
    model = 'raised'
    blg = '#F8F8FF'
    cfon = '#000000'
    larg_monitor = rp.winfo_screenwidth()
    alt_monitor = rp.winfo_screenheight()
    posix = larg_monitor / 2 - largura / 2
    posiy = alt_monitor / 2 - altura / 2
    rp.geometry("%dx%d+%d+%d" % (largura, altura, posix, posiy))
    rp.title('CÁLCULO MÉDIA v3.0')
    rp.configure(background='#000000')
    rp.resizable(True, True)
    rp.minsize(width=750,
               height=550)
    rp.iconbitmap("Images icons/document_blank.ico")
    disc = Menubutton(rp)
    disc.place(relx=0.300, rely=0.0055, relwidth=0.540, relheight=0.040)
    label_1 = Label(rp,
                    bd=7,
                    relief='sunken',
                    bg='#363636',
                    highlightbackground='#759fe6',
                    highlightthickness=3,
                    textvariable=texto,
                    font='Times 13',
                    fg='#F8F8FF',
                    anchor=NW,
                    padx=7,
                    pady=7,
                    justify=LEFT)
    label_1.place(relx=0.110, rely=0.100, relwidth=0.885, relheight=0.841)
    botao_1 = Button(rp,
                     bd=3,
                     relief=model,
                     bg=blg,
                     fg=cfon,
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Relatório')
    botao_1.place(relx=0.0055, rely=0.0055, relwidth=0.120, relheight=0.040)
    botao_2 = Button(rp,
                     bd=3,
                     relief=model,
                     bg=blg,
                     fg=cfon,
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Sair')
    botao_2.place(relx=0.8745, rely=0.9545, relwidth=0.120, relheight=0.040)
    botao_3 = Button(rp,
                     bd=3,
                     relief=model,
                     bg=blg,
                     fg=cfon,
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='% Aprovei.')
    botao_3.place(relx=0.0055, rely=0.9545, relwidth=0.120, relheight=0.040)
    botao_4 = Button(rp,
                     bd=3,
                     relief=model,
                     bg=blg,
                     fg=cfon,
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Editar')
    botao_4.place(relx=0.131, rely=0.9545, relwidth=0.120, relheight=0.040)
    botao_5 = Button(rp,
                     bd=3,
                     relief=model,
                     bg=blg,
                     fg=cfon,
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Cadastrar')
    botao_5.place(relx=0.2565, rely=0.9545, relwidth=0.120, relheight=0.040)
    botao_6 = Button(rp,
                     bd=3,
                     relief=model,
                     bg=blg,
                     fg=cfon,
                     highlightbackground='#759fe6',
                     highlightthickness=3,
                     text='Iteração')
    botao_6.place(relx=0.382, rely=0.9545, relwidth=0.120, relheight=0.040)
    texto.set('{}No dia seguinte, o príncipe anunciou que receberia, numa celebração especial,'
              'todas as pretendentes e lançaria um desafio. Uma velha senhora,'
              'serva do palácio há muitos anos, ouvindo os comentários sobre os preparativos,'
              'sentiu uma leve tristeza pois sabia que sua jovem filha nutria um sentimento'
              'de profundo amor pelo príncipe.'.format(largura))
    rp.mainloop()


root_principal()
