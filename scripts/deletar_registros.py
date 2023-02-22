import sqlite3

def deletar():
    nomeBanco = input('Qual é o nome do banco de dados: ')
    nomeTabela = input('Qual é o nome da tabela: ')
    conexao = sqlite3.connect(nomeBanco + '.db')
    cursor = conexao.cursor()
    try:
        cursor.execute('DELETE FROM ' + nomeTabela + ' WHERE ' + input('Qual é a coluna que voce deseja acessar: ') + ' = ' + input('O que deseja excluir dessa coluna: '))
        conexao.commit()
        conexao.close()
        print('Registro deletado com sucesso')
    except sqlite3.Error as erro:
        print('Houve um erro:',erro)