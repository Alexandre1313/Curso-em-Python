from random import randint
from time import sleep
print('\033[33m--=\033[m'*24)
com = int(input('Digite o início do intervalo:  '))
fin = int(input('Digite o final do intervalo :  '))
print(f'Vou pensar em um número entre \033[33m{com}\033[m e \033[33m{fin}\033[m, tente adivinhar...')
print('\033[33m--=\033[m'*24)
comp1 = jog1 = 0
res1 = ' '
while res1 != 'N':
    comp = randint(com, fin)
    res = int(input('Em que número eu pensei???:  '))
    print('\033[35mProcessando...\033[m')
    sleep(0.5)
    if comp == res:
        jog1 = jog1 + 1
        print(f'\033[33m:-) PARABÉNS!!! Você conseguiu me vencer, pois eu tembém escolhi \033[35m{comp}\033[m\033[m')
    else:
        comp1 = comp1 + 1
        print(f'\033[31m:-( Não foi dessa vez, tente de novo, pois eu escolhi \033[35m{comp}\033[m\033[m')
    res1 = str(input('Deseja continuar? [Qualquer tecla para continuar [N] para parar]:  ')).strip().upper()
    print('\033[33m--=\033[m' * 24)
print(f'''Obrigado por jogar comigo!!!
Você venceu {jog1} vezes, eu venci {comp1} vezes''')
