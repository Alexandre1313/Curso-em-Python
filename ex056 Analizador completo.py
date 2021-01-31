soma = maisv = cont = 0
nomeve = ''
for pess in range(1, 5):
    print('-=' * 20)
    print(f"\033[33m{pess}ª  pessoa\033[m")
    nome = str(input('\033[35mNome:  \033[m')).strip().upper()
    idade = int(input('\033[31mIdade:  \033[m'))
    sexo = str(input('\033[36mSexo [M/F]:  \033[m')).strip().upper()
    soma = soma + idade
    if pess == 1 and sexo in 'M':
        maisv = idade
        nomeve = nome
    if sexo in 'M' and idade > maisv:
        maisv = idade
        nomeve = nome
    if sexo == 'F' and idade < 20:
        cont = cont + 1
print('=-'*20)
media = soma / 4
print(f'A média de idade do grupo é \033[31m{media}\033[m anos')
print(f'O homem mais velho tem \033[31m{maisv}\033[m anos e se chama \033[31m{nomeve.lower().title()}\033[m')
print(f'No grupo temos \033[31m{cont}\033[m mulheres com menos de 20 anos')
