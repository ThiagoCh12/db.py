import sqlite3


conex = sqlite3.connect("estoque.db")
cursor = conex.cursor()

cursor.execute('''
                INSERT INTO tabProd(tbCod, tbNome, tbQtde, tbEstado)
                VALUES (4, "TECLADO", 15, "SP")''')
cursor.execute('''
                INSERT INTO tabProd(tbCod, tbNome, tbQtde, tbEstado)
                VALUES (2, "MONITOR", 12, "SP")''')
cursor.execute('''
                INSERT INTO tabProd(tbCod, tbNome, tbQtde, tbEstado)
                VALUES (3, "MOUSE", 9, "SP")''')           
conex.commit()
cursor.close()
conex.close()
