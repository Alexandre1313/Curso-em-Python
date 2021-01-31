mais18 = homi = mulher = 0
while True:
    print('-'*40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('-'*40)
    idade = int(input('Informe a idade:  '))
    sexo = str(input('Informe o sexo [M/F]:  ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo inválido, informe novamente [M/F]:  ')).strip().upper()[0]
    if idade > 18:
        mais18 = mais18 + 1
    if sexo == 'M':
        homi = homi + 1
    if sexo == 'F':
        if idade < 20:
            mulher = mulher + 1
    continu = str(input('Deseja continuar? [S/N]:  ')).strip().upper()[0]
    while continu not in 'SN':
        continu = str(input('Opção inválida, tente novamente [S/N]:  ')).strip().upper()[0]
    if continu == 'N':
        break
print('-'*40)
if mais18 > 0:
    print(f'Foram cadastradas {mais18} pessoas com mais de 18 anos de idade')
if homi > 0:
    print(f'Foi cadastrado o total de {homi} pessoa(s) do sexo masculino')
if mulher > 0:
    print(f'Neste grupo temos {mulher} mulher(es) com menos de 20 anos de idade')
