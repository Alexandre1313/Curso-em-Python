from random import shuffle
n1 = int(input('Primeiro valor:  '))
n2 = int(input('Segundo valor:  '))
n3 = int(input('Terceiro valor:  '))
n4 = int(input('Quarto valor:  '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem dos números ficou assim {lista}')
