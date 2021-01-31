import sqlite3

# Criar e ativar a base de dados
dbase = sqlite3.connect('dados.db')
c = dbase.cursor()  # Variável 'c' recebendo o cursor, navega dentro da base de dados
dbase.execute('''CREATE TABLE IF NOT EXISTS dados(
              CADASTRO INT PRIMARY KEY NOT NULL, 
              NOME TEXT NOT NULL)''')  # Cria a tabela se ela não existe com seus respectivos campos e tipos de dados
# Aplica as mudanças à base de dados
dbase.commit()
# Função que escreve  o Nome e ID dentro da base de dados


def escrever(cadastro, nome):
    c.execute('''INSERT into dados(CADASTRO, NOME) VALUES (?, ?)''', (cadastro, nome))
    dbase.commit()
