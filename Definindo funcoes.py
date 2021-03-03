"""
-Definindo funções
- Funções são pequenos trechos de código que realizam tarefas específicas
já utilizamos funções desde que iciciamos este curso
- Pode ou não receber entradas de dos e retornar ou não uma saída de dados
- obs : Se voc~e escrever uma função que realiza várias tarefas dentro dela é bom fazer uma verificaão
para que a função seja simplificada



cores = ['Azul', 'Amarelo', 'Vermelho', 'Branco', 'Preto']

print(cores)

cores.append('Roxo')

print(cores)

dici = {'1': cores[0], '2': cores[1], '3': cores[4]}

print(dici)
print(dici['2'])


def geradict(*args):
    contador = 1
    dicionario = {}
    for v in args:
        dicionario[contador] = v
        contador += 1

    return dicionario


a = geradict('Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber',
             'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12',
             'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3',
             'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown',
             'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkGreen',
             'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGrey',
             'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7',
             'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5',
             'DarkPurple6', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1',
             'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5',
             'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging',
             'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1',
             'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7',
             'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12',
             'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5',
             'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1',
             'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3',
             'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8',
             'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3',
             'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal',
             'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Reddit',
             'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal',
             'Tan', 'TanBlue', 'TealMono', 'Topanga')

dct2 = {1: 'Black', 2: 'BlueMono', 3: 'BluePurple', 4: 'BrightColors', 5: 'BrownBlue', 6: 'Dark', 7: 'Dark2',
        8: 'DarkAmber', 9: 'DarkBlack', 10: 'DarkBlack1', 11: 'DarkBlue', 12: 'DarkBlue1', 13: 'DarkBlue10',
        14: 'DarkBlue11', 15: 'DarkBlue12', 16: 'DarkBlue13', 17: 'DarkBlue14', 18: 'DarkBlue15', 19: 'DarkBlue16',
        20: 'DarkBlue17', 21: 'DarkBlue2', 22: 'DarkBlue3', 23: 'DarkBlue4', 24: 'DarkBlue5', 25: 'DarkBlue6',
        26: 'DarkBlue7', 27: 'DarkBlue8', 28: 'DarkBlue9', 29: 'DarkBrown', 30: 'DarkBrown1', 31: 'DarkBrown2',
        32: 'DarkBrown3', 33: 'DarkBrown4', 34: 'DarkBrown5', 35: 'DarkBrown6', 36: 'DarkGreen', 37: 'DarkGreen1',
        38: 'DarkGreen2', 39: 'DarkGreen3', 40: 'DarkGreen4', 41: 'DarkGreen5', 42: 'DarkGreen6', 43: 'DarkGrey',
        44: 'DarkGrey1', 45: 'DarkGrey2', 46: 'DarkGrey3', 47: 'DarkGrey4', 48: 'DarkGrey5', 49: 'DarkGrey6',
        50: 'DarkGrey7', 51: 'DarkPurple', 52: 'DarkPurple1', 53: 'DarkPurple2', 54: 'DarkPurple3', 55: 'DarkPurple4',
        56: 'DarkPurple5', 57: 'DarkPurple6', 58: 'DarkRed', 59: 'DarkRed1', 60: 'DarkRed2', 61: 'DarkTanBlue',
        62: 'DarkTeal', 63: 'DarkTeal1', 64: 'DarkTeal10', 65: 'DarkTeal11', 66: 'DarkTeal12', 67: 'DarkTeal2',
        68: 'DarkTeal3', 69: 'DarkTeal4', 70: 'DarkTeal5', 71: 'DarkTeal6', 72: 'DarkTeal7', 73: 'DarkTeal8',
        74: 'DarkTeal9', 75: 'Default', 76: 'Default1', 77: 'DefaultNoMoreNagging', 78: 'Green', 79: 'GreenMono',
        80: 'GreenTan', 81: 'HotDogStand', 82: 'Kayak', 83: 'LightBlue', 84: 'LightBlue1', 85: 'LightBlue2',
        86: 'LightBlue3', 87: 'LightBlue4', 88: 'LightBlue5', 89: 'LightBlue6', 90: 'LightBlue7', 91: 'LightBrown',
        92: 'LightBrown1', 93: 'LightBrown10', 94: 'LightBrown11', 95: 'LightBrown12', 96: 'LightBrown13',
        97: 'LightBrown2', 98: 'LightBrown3', 99: 'LightBrown4', 100: 'LightBrown5', 101: 'LightBrown6',
        102: 'LightBrown7', 103: 'LightBrown8', 104: 'LightBrown9', 105: 'LightGray1', 106: 'LightGreen',
        107: 'LightGreen1', 108: 'LightGreen10', 109: 'LightGreen2', 110: 'LightGreen3', 111: 'LightGreen4',
        112: 'LightGreen5', 113: 'LightGreen6', 114: 'LightGreen7', 115: 'LightGreen8', 116: 'LightGreen9',
        117: 'LightGrey', 118: 'LightGrey1', 119: 'LightGrey2', 120: 'LightGrey3', 121: 'LightGrey4',
        122: 'LightGrey5', 123: 'LightGrey6', 124: 'LightPurple', 125: 'LightTeal', 126: 'LightYellow',
        127: 'Material1', 128: 'Material2', 129: 'NeutralBlue', 130: 'Purple', 131: 'Reddit', 132: 'Reds',
        133: 'SandyBeach', 134: 'SystemDefault', 135: 'SystemDefault1', 136: 'SystemDefaultForReal', 137: 'Tan',
        138: 'TanBlue', 139: 'TealMono', 140: 'Topanga'}


print(a)

b = geradict()

"""


def ordem_dos_parametros(nome, *args, idade, **kwargs):
    print(nome)
    print(args)
    print(idade)
    print(kwargs)


ordem_dos_parametros('alexandre', 6, 9, 9, idade=99, pf='Pedro')
