from random import randint
vi = 0
while True:
    jogador = int(input('Digite um valor:  '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = str(input('Par ou Ímpar? [P/I]:  ')).strip().upper()[0]
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]:  ')).strip().upper()[0]
    print('=-' * 26)
    print(f'Você jogou {jogador} e o computador jogou {computador}, total de {total}')
    print('Deu par'if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu, parabéns!!!')
            print('=-' * 26)
            vi = vi + 1
        else:
            print('Você perdeu GAME OVER')
            print('=-' * 26)
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu, parabéns!!!')
            print('=-' * 26)
            vi = vi + 1
        else:
            print('Você perdeu GAME OVER')
            print('=-' * 26)
            break
    print('Vamos jogar novamente?')
print(f'Você venceu {vi} vez(es)')
