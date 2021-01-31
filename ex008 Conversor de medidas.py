medida = float(input('Digite uma medida em metros:  '))
print(f'''A medida informada corresponde á \033[32m{medida * 1000}\033[m mm
Corresponde também á \033[32m{medida * 100}\033[m cm
Corresponde também á \033[32m{medida * 10}\033[m dm
Corresponde também á \033[32m{medida}\033[m m
Corresponde também á \033[32m{medida / 10}\033[m dam
Corresponde também á \033[32m{medida / 100}\033[m hm
E corresponde por último também á \033[32m{medida / 1000}\033[m km''')
