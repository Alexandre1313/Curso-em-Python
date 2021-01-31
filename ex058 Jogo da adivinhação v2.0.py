from random import randint
computador = randint(0, 13)
print('=-'*30)
print('''\033[33mOlá!Sou seu computador...
Acabei de pensar em um número de 0 a 13, tente advinhar...
Vamos lá, de o seu palpite...\033[m''')
print('-='*30)
contador = 0
jogador = -1
while jogador != computador:
    jogador = int(input(f'Seu {contador + 1}º palpite:  '))
    contador = contador + 1
    if computador < jogador:
        print('\033[32mMenos\033[m\033[31m....\033[m')
    elif computador > jogador:
        print('\033[32mMais\033[m\033[31m....\033[m')
print('=-'*30)
if contador <= 5:
    print(f'Parabéns, eu havia escolhido {computador} e você me venceu na {contador}ª tentativa')
elif 5 < contador <= 10:
    print(f'Você foi regular, eu havia escolhido {computador} e você me venceu na {contador}ª tentativa')
elif contador > 10:
    print(f'Você foi péssimo, eu havia escolhido {computador} e você me venceu na {contador}ª tentativa')
