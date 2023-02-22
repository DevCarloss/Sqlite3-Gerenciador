import sqlite3

def criadorDados():
    nomeBanco = input('Qual é o nome do banco de dados: ')
    conexao = sqlite3.connect(nomeBanco + '.db')
    cursor = conexao.cursor()
    try:
        nomeTabela = input('Qual é o nome da tabela para inserir os valores: ')
        valores = input('Quais são os valores: ')
        cursor.execute('INSERT INTO ' + nomeTabela + ' VALUES(' + valores + ')')
        conexao.commit()
        print('Valores adicionados com sucesso!!')
    except sqlite3.Error as erro:
        print('Erro ao adicionar dados:' , erro)