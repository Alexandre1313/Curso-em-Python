from ex115.lib.interface import *


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mERRO ao ler o arquivo!!\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!!\033[m')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO ao ler o arquivo!!\033[m')
    else:
        cabecalho('Pessoas cadastradas')
        for linhas in a:
            dado = linhas.split(';')
            dado[1] = dado[1].replace('\n', '')
            if dado[1] == '1':
                print(f'\033[35m{dado[0]:<30}\033[m\033[34m{dado[1]:>3} ano\033[m')
            else:
                print(f'\033[35m{dado[0]:<30}\033[m\033[34m{dado[1]:>3} anos\033[m')
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO, não foi possível abrir o arquivo!!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO na gravação dos dados!!\033[m')
        else:
            print(f'\033[32mNovo registro de {nome} adicionado com sucesso!!\033[m')
        a.close()
