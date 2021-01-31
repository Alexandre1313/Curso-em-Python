from datetime import date
atual = date.today().year
contme = contma = 0
for i in range(1, 8):
    idade = int(input(f'Digite o ano de nascimento da {i}ª pessoa:  '))
    vida = atual - idade
    if vida <= 21:
        contme = contme + 1
    else:
        contma = contma + 1
print(f'\033[32mAo todo tivemos {contma} pessoas maiores de idade\033[m')
print(f'\033[33mE também tivemos {contme} pessoas menores de idade\033[m')
