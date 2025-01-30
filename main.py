import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

global somaTotal
somaTotal = 0 

processo = int(input("Qual e o processo a ser feito ?\n[1] - Somar compras\n"))

def somarCompras(produto,):
    global valorSoma
    cursor.execute('SELECT valorFixo FROM produtos WHERE ID = ?', (produto, ))
    valorProduto = cursor.fetchone()
    valorSoma = int(valorProduto[0])
    


if processo == 1:
    cursor.execute('SELECT id FROM produtos ORDER BY id DESC LIMIT 1')
    maximo = cursor.fetchone()
    limite = int(maximo[0])
    valorProduto = [limite]
    i = 0
    
    while i < limite:
      try:
        produto = int(input("Digite o ID do produto\n"))
        somarCompras(produto)
        somaTotal += valorSoma
        i += 1
      except produto > limite or produto < limite :
        print("Por favor, insira um número válido para o ID do produto.")

        
print(f"O valor total da compra é de: R${somaTotal}")        


