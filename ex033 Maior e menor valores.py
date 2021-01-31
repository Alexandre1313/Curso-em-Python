n1 = float(input('Digite o primeiro valor:  '))
n2 = float(input('Digite o segundo valor:  '))
n3 = float(input('Digite o terceiro valor:  '))
menor = n1
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
