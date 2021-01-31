def voto(ano=0):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano
    if 18 <= idade < 65:
        return f'Com a idade de {idade} anos, o voto é obrigatório!!!'
    elif idade >= 65 and idade != atual or 16 <= idade < 18 and idade != atual:
        return f'Com a idade de {idade} anos, o voto é opcional!!!'
    elif idade < 16:
        return f'Com a idade de {idade} anos, você ainda não atingiu a idade de votar!!!'
    elif ano == 0:
        return f'Ano de nascimento não informado!!!'


print(voto(2006))
