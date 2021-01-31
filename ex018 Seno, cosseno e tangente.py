from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo desejado:  '))
sen = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))
print(f'''O ângulo de {ang} tem o Seno de {sen:.2f}
O ângulo de {ang} tem o Cosseno de {cose:.2f}
O ângulo de {ang} tem a Tangente de {tang:.2f}''')
