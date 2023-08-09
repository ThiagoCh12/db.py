import sqlite3 as sql

db = "estoque.db"

con = sql.connect(db)
cursor = con.cursor()

x = "s"

inserir = 'n'
while(x.lower() == 's'):

    try:
        w_cod = int(input("Codigo do prod: "))


        w_nome = input("Nome: ")
      

        w_qtde = int(input("Quantidade: "))

        w_estado = input("Estado: ")

        cursor.execute('''
                INSERT INTO tabProd(tbCod, tbNome, tbQtde, tbEstado)
                VALUES (?,?,?,?)''', (w_cod, w_nome, w_qtde, w_estado))

        inserir = 's'
    except sql.IntegrityError:
        print("==> Chave existente", w_cod)

    
    x = input("Deseja continuar? (s/n): ")
    if inserir.lower() == 's':
        con.commit()

    cursor.close()
    con.close()