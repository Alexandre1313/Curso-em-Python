import random
pri = str(input('Nome do primeiro aluno:  '))
seg = str(input('Nome do segundo aluno: '))
terc = str(input('Nome do terceiro aluno:  '))
quar = str(input('Nome do quarto aluno:  '))
quin = str(input('Nome do quinto aluno:  '))
lista = [pri, seg, terc, quar, quin]
alu = random.choice(lista)
print(f'O aluno escolhido foi {alu}')
