nome = str(input('Digite seu nome completo:  ')).strip().lower().title()
div = nome.split()
print(f'Seu nome completo é {nome}')
print(f'Seu primeiro nome é {div[0]}')
print(f'Seu último nome é {div[len(div) - 1]}')  # nome splitado em uma lista no caso div
# o último nome é div na posição de leitura (len) de div - 1 , pra ficar de traz pra frente, e menos
# 1 por que o len de div é 6, porem como o Python conta a partir do zero nao há posiçao 6, por isso menos 1
# pra cai na posição 5.
