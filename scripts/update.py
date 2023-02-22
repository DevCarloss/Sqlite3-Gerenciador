import sqlite3

def alterar():
    nomeBanco = input('Qual é o nome do banco de dados: ')
    conexao = sqlite3.connect(nomeBanco + '.db')
    cursor = conexao.cursor()
    tabela = input('Qual é o nome da tebela: ')
    coluna = input('Qual é o nome da coluna que voce quer alterar: ')
    try:
        cursor.execute('UPDATE ' + tabela  + ' SET ' + coluna + '= ' + input('Qual é o valor que voce deseja adicionar: ') + ' WHERE '+ coluna + '= ' + input('Valor a ser substituído: '))
        conexao.commit()
        print('Valores alterados com sucesso!')
    except sqlite3.Error as erro:
        print("Sqlite Erro:",erro)
        