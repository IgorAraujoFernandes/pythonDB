import sqlite3
from tkinter import *
from tkinter import ttk

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

processo = int(input("Qual e o processo a ser feito ?\n [1] - Somar compras\n "))

# processo = int(input('O que deseja fazer ?\n [1] '))

# cursor.execute('CREATE TABLE produtos(ID int NOT NULL PRIMARY KEY, nomeProduto varchar(50) NOT NULL, categoria varchar(50) NOT NULL, refrigerado bit NOT NULL, alcoolico bit NOT NULL )')

# cursor.execute('INSERT INTO produtos(ID, nomeProduto, categoria, refrigerado, alcoolico) VALUES(1, "LeiteIntegral", "Bebidas", 1, 0), (2, "LeiteDesnatado", "Bebidas", 1, 0), (3, "Biscoito", "Alimentos", 0, 0), (4, "Cerveja", "Bebidas", 1, 1), (5, "Picanha", "Carnes", 1, 0)')

# banco.commit()

# cursor.execute('ALTER TABLE produtos ADD valorFixo int')

# cursor.execute('UPDATE produtos SET valorFixo = 5 WHERE nomeProduto = "leiteIntegral"')
# cursor.execute('UPDATE produtos SET valorFixo = 5 WHERE nomeProduto = "leiteDesnatado"')
# banco.commit()
# cursor.execute('UPDATE produtos SET valorFixo = 3 WHERE nomeProduto = "Biscoito"')
# cursor.execute('UPDATE produtos SET valorFixo = 10 WHERE nomeProduto = "Cerveja"')
#cursor.execute('UPDATE produtos SET valorFixo = 50 WHERE nomePRoduto = "Picanha"') 

if processo == 1:
    print("teste")

cursor.execute('SELECT valorFixo FROM produtos WHERE nomeProduto = "Picanha"') 
resultado = cursor.fetchone()
valor1 = int(resultado[0])

cursor.execute('SELECT valorFixo FROM produtos WHERE nomeProduto = "Cerveja"')
resultado = cursor.fetchone()
valor2 = int(resultado[0])

print ("o valor total e: ")
print (valor1 + valor2)

# print (preco1, preco2)

# cursor.execute('SELECT * FROM produtos')

# print(cursor.fetchall())