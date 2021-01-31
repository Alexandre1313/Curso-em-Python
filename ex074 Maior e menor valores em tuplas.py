from random import randint
valores = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999))
print(f'Os valores sorteados foram: {valores}')
print(f'O menor valor da lista é: {min(valores)}')
print(f'O maior valor da lista é: {max(valores)}')
print('=-'*27)
valores = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999))
numer = valores
men = mai = 0
for c in range(0, 5):
    if c == 0:
        mai = numer[c]
        men = numer[c]
    else:
        if numer[c] > mai:
            mai = numer[c]
        if numer[c] < men:
            men = numer[c]
print(f'Os valores sorteados foram: {valores}')
print(f'O menor valor da lista é: {men}')
print(f'O maior valor da lista é: {mai}')
