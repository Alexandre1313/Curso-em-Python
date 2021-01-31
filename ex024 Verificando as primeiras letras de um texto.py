cid = str(input('Que cidade você nasceu?:  ')).strip().lower().title()
cid1 = cid.split()
resul = 'Santo' in cid1[0]
if resul is True:
    print(f'A cidade de {cid} começa com a palavra "Santo"')
else:
    print(f'A cidade de {cid} não começa com a palavra "Santo"')
print(cid[:5].upper() == 'SANTO')  # o print retorna true ou false, pois esta
# perguntando se a string da posição zero até a quatro é igual á santo.
