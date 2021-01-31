nome = str(input('Digite seu nome completo:  ')).strip().lower().title()
nome1 = nome.split()
resul = 'Silva' in nome1
if resul is True:
    print(f'O nome {nome} possui "Silva" em sua formação')
else:
    print(f'O nome {nome} não possui "Silva" em sua formação')
print('Seu nome tem "Silva" ? {}'.format('Silva' in nome1))  # se eu por silva in nome ao
# invés de nome1 se eu digitar silvana ele dira true ao invés de false
# se eu esplitar primeiro e depois comparar com nome1 esplitado eu elimino
# essa possibilidade .
