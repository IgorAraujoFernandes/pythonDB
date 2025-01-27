import sqlite3
# from tkinter import *
# from tkinter import ttk

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

# cursor.execute('CREATE TABLE produtos(ID int NOT NULL PRIMARY KEY, nomeProduto varchar(50) NOT NULL, categoria varchar(50) NOT NULL, refrigerado bit NOT NULL, alcoolico bit NOT NULL )')

cursor.execute('INSERT INTO produtos(ID, nomeProduto, categoria, refrigerado, alcoolico) VALUES(1, "LeiteIntegral", "Bebidas", 1, 0), (2, "LeiteDesnatado", "Bebidas", 1, 0), (3, "Biscoito", "Alimentos", 0, 0), (4, "Cerveja", "Bebidas", 1, 1), (5, "Picanha", "Carnes", 1, 0)')

cursor.execute('SELECT * FROM produtos')

print(cursor.fetchall())