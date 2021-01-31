print('-' * 40)
print(f'{"LOJAS SUPER BARATÃO":^40}')
print('-' * 40)
total = produto1000 = menosb = cont = 0
nomepro = ''
while True:
    produto = str(input('Produto:  '))
    preco = float(input('Valor:R$  '))
    print('-'*40)
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        produto1000 = produto1000 + 1
    if cont == 1 or preco < menosb:
        menosb = preco
        nomepro = produto
    pcao = str(input('Deseja continuar? [S/N]:  ')).strip().upper()[0]
    while pcao not in 'SN':
        pcao = str(input('Deseja continuar? [S/N]:  ')).strip().upper()[0]
    print('-'*40)
    if pcao == 'N':
        break
print(f'O valor total de sua compra foi R$ {total:.2f}')
print(f'Nesta lista de compras há {produto1000} produto(s) com valor acima de R$ 1000,00')
print(f'O produto mais barato é o(a) {nomepro} custando R$ {menosb:.2f}')
