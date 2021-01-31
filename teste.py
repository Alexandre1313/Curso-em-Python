lista = list()
listg = []
while True:
    lista.append(int(input('Código da cor:  ')))
    lista.append(str(input('Cor:  ')))
    lista.append(str(input('Descrição:  ')))
    listg.append(lista[:])
    lista.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar:  ')).upper()
    if resp == 'N':
        break
print(listg)
