from ex115.lib.arquivo import *
arq = 'Cadastro.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)
while True:
    resposta = menu(['Cadastrar pessoas', 'Listar pessoas cadastradas', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('Novo cadastro:')
        res = ' '
        while res != 'N':
            nome = str(input('\033[37mInforme o nome da pessoa a ser cadastrada:\033[m  ')).strip().lower().title()
            idade = leiainteiro('\033[37mInforme a idade:\033[m  ')
            cadastrar(arq, nome, idade)
            res = str(input('\033[37mDeseja cadastrar mais pessoas? [S/N]:\033[m  ')).strip().upper()
            while res not in 'SN':
                res = str(input('\033[37mDeseja cadastrar mais pessoas? [S/N]:\033[m  ')).strip().upper()
    elif resposta == 2:
        ler_arquivo(arq)
    elif resposta == 3:
        cabecalho('Saindo do sistema, até logo!!')
        break
    else:
        print('\033[31mERRO!Por favor selecione uma opção válida!!\033[m')
