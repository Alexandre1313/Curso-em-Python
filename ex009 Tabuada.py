numero = float(input('Digite um número para ver sua tabuada:  '))
cont = 0
for c in range(1, 1133):
    cont = cont + 1
    print(f"{c:2} x {numero:2} = {c * numero:2.2f}")
