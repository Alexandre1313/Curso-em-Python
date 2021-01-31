lista = ('CANETA', 1.99, 'LÁPIS', 0.59, 'CADERNO', 13.97, 'BORRACHA', 0.49, 'RÉGUA', 2.69, 'MOCHILA', 24.99,
         'LÁPIS DE COR', 15.99, 'PINCÉL', 4.39, 'TRANSFERIDOR', 5.99, 'COMPASSO', 3.99, 'APONTADOR', 5.79,
         'TINTA GUACHE', 7, 'LAPISEIRA', 2.99)
print('=-'*20)
print(f'{"LISTA DE PREÇOS PAPELARIA CV":^40}')
print('-='*20)
soma = 0
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'\033[31m{lista[c]:_<30} R$', end='')
    else:
        print(f'{lista[c]:>7.2f}\033[m')
        soma = soma + lista[c]
print('=-'*20)
print(f'{"Total":_<30} R$', end='')
print(f'{soma:>7.2f}')
