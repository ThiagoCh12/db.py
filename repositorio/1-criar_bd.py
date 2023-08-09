import sqlite3


conex = sqlite3.connect("estoque.db")  #cria conexao com o banco

cursor = conex.cursor()  #enviar comandos para o banco

#Executar comando
cursor.execute('''   
            CREATE TABLE tabProd(tbCod INTEGER PRIMARY KEY, 
            TbNome TEXT, 
            tbQtde INTEGER, 
            tbEstado TEXT)''')
cursor.close() # fechar cursor
conex.close()  # fecha conexao com o banco