frase = str(input('Digite uma frase:  ')).strip().upper()
sep = frase.split()
junto = ''.join(sep)
nomec = ''
junto1 = ' '.join(sep)
nomec1 = ''
for c in range(len(junto), 0, -1):
    nomec = nomec + junto[c - 1]
for c in range(len(junto1), 0, -1):
    nomec1 = nomec1 + junto1[c - 1]
if junto == nomec:
    print(f'A frase digitada foi: \033[35m{junto1}\033[m')
    print(f'A frase ao contrário é: \033[33m{nomec1}\033[m')
    print(f'Tudo junto: [\033[36m{junto}\033[m]  ->  [\033[32m{nomec}\033[m]')
    print('\033[32mTEMOS UM PALÍNDROMO\033[m')
else:
    print(f'A frase digitada foi: \033[35m{junto1}\033[m')
    print(f'A frase ao contrário é: \033[33m{nomec1}\033[m')
    print(f'Tudo junto: [\033[36m{junto}\033[m]  ->  [\033[32m{nomec}\033[m]')
    print('\033[31mNÃO TEMOS UM PALÍNDROMO\033[m')
