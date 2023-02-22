import sqlite3

def criadorTabela():
    print('Criador de Banco de Dados')
    
    # Criar Banco de dados 
    nomeBanco = input('Como deseja chamar seu Banco de dados: ')
    conexao =  sqlite3.connect(nomeBanco + '.db')
    cursor = conexao.cursor()
    
    # Criar Tabelas
    nometabela = input('Qual será o nome da sua tabela: ')
    try:
     cursor.execute("CREATE TABLE " + nometabela + '(' + input("Quais será os nomes & tipos da coluna: ") + ')')
     print('Tabela e colunas criadas com sucesso!!')
    
    except sqlite3.Error as erro:
      print("Erro ao criar a tabela:" ,  erro)
      conexao.close()

