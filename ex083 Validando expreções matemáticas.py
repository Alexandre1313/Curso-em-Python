lista = list()
listaf = list()
listag = list()
paren = str(input('\033[33mDigite uma expressão matemática:\033[m  '))
lista.append(paren)
for palavras in lista:
    for paren in palavras:
        if paren == '(':
            listaf.append(paren)
        elif paren == ')':
            listag.append(paren)
if len(listaf) == len(listag):
    print('\033[32mA expressão digitada é válida!!!\033[m')
else:
    print('\033[31mA expressão digitada é inválida!!!\033[m')
