import sqlite3

conex = sqlite3.connect("estoque.db")

cursor = conex.cursor()

cursor.execute("SELECT tbCod, tbNome, tbQtde FROM tabProd")

linha = cursor.fetchone()

for elemento in linha:
    print(elemento)

cursor.close()
conex.close()