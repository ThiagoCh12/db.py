import sqlite3


conex = sqlite3.connect("estoque.db")

cursor = conex.cursor()

cursor.execute("SELECT * FROM tabProd")

linha = cursor.fetchall()
for elemento in linha:
    print (elemento)

cursor.close()
conex.close()