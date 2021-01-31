temp = float(input('Informe a temperatura em °C:  '))
far = temp * 1.8 + 32
print(f'A temperatura de \033[31m{temp:.1f}\033[m°Celcius convertida para Fahrenheit fica \033[31m{far:.1f}\033[m°F')
tem1 = float(input('Informe a temperatura em °F:  '))
cel = (tem1 - 32) / 1.8
print(f'A temperatura de \033[31m{tem1:.1f}\033[m°Fahrenheit convertida para Celsius fica \033[31m{cel:.1f}\033[m°C')
