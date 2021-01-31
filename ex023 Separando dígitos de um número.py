num = int(input('Digite um número:  '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
umi = num // 1000000 % 10
dmi = num // 10000000 % 10
cmi = num // 100000000 % 10
ubi = num // 1000000000 % 10
dbi = num // 10000000000 % 10
cbi = num // 100000000000 % 10
utri = num // 1000000000000 % 10
dtri = num // 10000000000000 % 10
ctri = num // 100000000000000 % 10
uqua = num // 1000000000000000 % 10
print(f'Unidade              : {u}')
print(f'Dezena               : {d}')
print(f'Centena              : {c}')
print(f'Unidade de milhar    : {um}')
print(f'Dezena de milhar     : {dm}')
print(f'Centena de milhar    : {cm}')
print(f'Unidade de milhão    : {umi}')
print(f'Dezena de milhão     : {dmi}')
print(f'Centena de milhão    : {cmi}')
print(f'Unidade de bilhão    : {ubi}')
print(f'Dezena de bilhão     : {dbi}')
print(f'Centena de bilhão    : {cbi}')
print(f'Unidade de trilhão   : {utri}')
print(f'Dezena de trilhão    : {dtri}')
print(f'Centena de trilhão   : {ctri}')
print(f'Unidade de quatrilhão: {uqua}')
