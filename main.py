import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

global somaTotal, maximo, limite
somaTotal = 0 
cursor.execute('SELECT id FROM produtos ORDER BY id DESC LIMIT 1')
maximo = cursor.fetchone()
limite = int(maximo[0])

processo = int(input("Qual e o processo a ser feito ?\n[1] - Somar compras\n[2] - Inserir produto novo\n"))

def somarCompras(produto,):
    global valorSoma
    cursor.execute('SELECT valorFixo FROM produtos WHERE ID = ?', (produto, ))
    valorProduto = cursor.fetchone()
    valorSoma = int(valorProduto[0])
    
def inserirProduto():
    nome = input("Digite o nome do produto novo:\n")
    categoria = input("Digite a categoria do produto:\n")
    refrigerado = int(input("É refrigerado ?\n[1] - Sim     [2] - Não\n"))
    if refrigerado == 2:
      refrigerado = 0
    alcoolico = int(input("É alcoolico? \n[1] - Sim     [2] - Não\n"))
    if alcoolico == 2:
      alcoolico = 0
    quantidade = int(input("Digite a quantidade inicial de produtos:\n"))
    valorFixo = int(input("Digite o valor inicial do produto:\n"))
    
    nvID = limite + 1

    cursor.execute('INSERT INTO produtos ("ID", "nomeProduto", "categoria", "refrigerado", "alcoolico", "quantidade", "valorFixo") VALUES(?, ?, ?, ?, ?, ?, ?)',(nvID, nome, categoria, refrigerado, alcoolico, quantidade, valorFixo, ))
    banco.commit()
    linhas_afetadas = banco.total_changes
    print(f'O número de linhas afetadas pela operação foi: {linhas_afetadas}')
    cursor.execute('SELECT * FROM produtos WHERE ID = ?', (nvID, ))
    print(cursor.fetchall())
     
if processo == 1:
        valorProduto = [limite]
        i = 0
        
        while i < limite:
      
            produto = int(input("Digite o ID do produto\n"))
            somarCompras(produto)
            somaTotal += valorSoma
            i += 1
            if produto > limite or produto < 1 :
              print("Por favor, insira um número válido para o ID do produto.")
        print(f"O valor total da compra é de: R${somaTotal}")        

if processo == 2:
  inserirProduto()
  


