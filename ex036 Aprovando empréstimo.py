vc = float(input('Qual o valor da imóvel:R$  '))
rc = float(input('Qual a renda do comprador:R$  '))
ano = int(input('Qual o prazo para pagamento [anos]:  '))
prazo = ano * 12
parc = vc / prazo
porc = rc * 30 / 100
if parc <= porc:
    print(f'''O empréstimo para compra do imóvel no valor de R$ {vc:.2f} foi concedido.
O valor das parcelas serão {prazo} vezes de R$ {parc:.2f}''')
else:
    print(f'''O empréstimo para compra do imóvel no valor de R$ {vc:.2f} foi negado.
Motivo:O valor de R$ {parc:.2f} referente às parcelas ultrapassa o limite de 30% da renda que é de R$ {rc:.2f}''')
