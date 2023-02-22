import sqlite3 

def visualizarbancodedados():
    coluna = input('Qual coluna voce deseja visualizar: ')
    nomeBanco = input('Qual nome do banco de dados: ')
    conexao = sqlite3.connect(nomeBanco + '.db')
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT ' + coluna + ' FROM ' + input('Nome da Tabela: '))
        print(cursor.fetchall())
    except sqlite3.Error as erro:
        print("Sqlite Erro:",erro)
    