altura = float(input('Informe a altura da parede à ser pintada:  '))
largura = float(input('Agora informe a largura da parede à ser pintada:  '))
area = altura * largura
litros = area / 2
print(f'As medidas de \033[33m[{altura:.2f}]\033[m m X \033[33m[{largura:.2f}]\033[m m correspondem ', end='')
print(f'à uma área total de \033[33m[{area:.2f}]\033[m m²')
print(f'Portanto necessitará de \033[33m[{litros:.2f}]\033[m litro(s) de tinta para ser pintada')
