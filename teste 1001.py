matriz = [[0, 0, 0, 0, 0, 0, 0, 0], [0 , 0, 0, 0, 0, 0, 0, 0], [0 , 0, 0, 0, 0, 0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 8):
        matriz[l][c] = int(input('Digite um valor:  '))
print(matriz)
for l in range(0, 3):
    for c in range(0, 8):
        print(matriz[l][c])
