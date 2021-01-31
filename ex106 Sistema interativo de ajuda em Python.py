c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m')


def ajuda(coman):
    titulo(f'Acessando o manual do comando / biblioteca: \'{coman}\'', 1)
    print(c[6])
    help(f'{coman}')
    print(c[0])


def titulo(msg, cor=0):
    tam = len(msg) + 6
    print(c[cor], end='')
    print('=' * tam)
    print(f'   {msg.strip().upper()}')
    print('=' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca:  ')).strip().lower()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Obrigado, volte sempre', 4)
