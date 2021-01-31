def escreva(msg):
    tam = len(msg.strip()) + 4
    print('\033[33m=\033[m' * tam)
    print(f'  {msg.strip()}')
    print('\033[33m=\033[m' * tam)


escreva('Alexandre Cordeiro')
escreva('a nota do aluno que chegou atrasado foi:')
escreva('oi')
escreva('         Frases de Grandes Gênios do Mundo. Mensagens, pensamentos e frases curtas de Grandes     ')
escreva('eu sou forte e amo à Deus')
