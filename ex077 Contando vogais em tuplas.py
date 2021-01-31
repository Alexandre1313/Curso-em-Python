palavras = ('Paython', 'Programador', 'Tuplas', 'Listas', 'Dicionários', 'If', 'Elif', 'Else', 'For', 'While',
            'True', 'False', 'Range', 'Enumerate', 'Computador', 'Input', 'Float', 'Int', 'String', 'Fatiamento',
            'Booleano', 'And', 'Or', 'Not in', 'Len', 'Mouse', 'Disco rígido', 'Estabilizador', 'Função', 'Global',
            'Texto', 'Um', 'Conjunto', 'Palavras', 'Frases', 'Encadeadas', 'Permitem', 'Interpretação', 'Transmitem',
            'Uma', 'Mensagem', 'Qualquer', 'Obra', 'Escrita', 'Versão', 'Original', 'Constitui', 'Livro', 'Documento',
            'Escrito', 'Unidade', 'Linguística', 'Extensão', 'Superior', 'Príncipe', 'Abacate')
cont = contu = contt = 0
for p in palavras:
    print(f'\nNa palavra {p.upper():_<17} {"temos:":_<15}', end='')
    for letra in p:
        if letra.lower() in 'eiío':
            print(f'\033[32m{letra.upper():>2}\033[m', end='')
        if letra.lower() in 'aáàãâ':
            print(f'\033[35m{letra.upper():>2}\033[m', end='')
            cont = cont + 1
        if letra.lower() in 'u':
            print(f'\033[33m{letra.upper():>2}\033[m', end='')
            contu = contu + 1
        if letra.lower() in 't':
            print(f'\033[31m{letra.upper():>2}\033[m', end='')
            contt = contt + 1
print()
print('=-'*29)
print(f'Esta tupla contém {len(palavras)} palavras')
print(f'Temos o total de {cont} letras A, {contu} letras U e {contt} letras T')
