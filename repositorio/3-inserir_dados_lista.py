import sqlite3 as sql

lista = [(10, "Tonner", 40, "SP"), (11, "Tablet", 10, "PR")]

con = sql.connect("estoque.db")

cursor = con.cursor()

cursor.executemany('''

        INSERT INTO tabProd(tbCod, tbNome, tbQtde, tbEstado)
        VALUES(?,?,?,?)''', lista)

con.commit()
cursor.close()
con.close()