import sqlite3
from tkinter import *
from tkinter import ttk

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

processo = int(input("Qual e o processo a ser feito ?\n[1] - Somar compras\n "))

if processo == 1:
    print 

cursor.execute('SELECT valorFixo FROM produtos WHERE nomeProduto = "Picanha"') 
resultado = cursor.fetchone()
valor1 = int(resultado[0])

cursor.execute('SELECT valorFixo FROM produtos WHERE nomeProduto = "Cerveja"')
resultado = cursor.fetchone()
valor2 = int(resultado[0])

print ("o valor total e: ")
print (valor1 + valor2)


