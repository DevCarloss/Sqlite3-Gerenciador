# Sqlite3 Python 
print('Bem vindo ao gerenciador de banco de dados sqlite')

# Opcoes
gerenciadorOpcoes = '[1] Criar Tabelas & Adicionar Colunas' + '\n' + '[2] Adicionar valores nas colunas' + '\n' + '[3] Visulizar Banco de dados' + '\n' + '[4] Deletar registros da tabela' + '\n' + '[5] Alterar registros da tabela' 
print(gerenciadorOpcoes)
input_usuario = input('Qual opcao voce deseja hoje: ')

# Criar Tabelas & Colunas
if int(input_usuario) == 1:
    from scripts import criadorTabela
    if __name__ == '__main__':
      criadorTabela.criadorTabela()

# Adicionar Valores 
elif (int(input_usuario) == 2):
   from scripts import dados
   if __name__ == '__main__':
      dados.criadorDados()

# Visulizar Banco de dados
elif int(input_usuario) == 3:
   from scripts import visualizar
   if __name__ == '__main__':
      visualizar.visualizarbancodedados()

# Deletar Registros 
elif int(input_usuario) == 4:
   from scripts import deletar_registros
   if __name__ == '__main__':
      deletar_registros.deletar()

# Alterar Registros 
elif int(input_usuario) == 5:
   from scripts import update
   if __name__ == '__main__':
      update.alterar()