import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

global somaTotal, maximo, limite, preço

somaTotal = 0
preço = 0 
cursor.execute('SELECT id FROM produtos ORDER BY id DESC LIMIT 1')
maximo = cursor.fetchone()
limite = int(maximo[0])


def somarCompras(produto, ):
   

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
    
def consultarPreco():

  global preço
  IDproduto = int(input("Digite o ID do produto a ser consultado:\n"))
  cursor.execute("SELECT valorFixo FROM produtos WHERE ID = ?", (IDproduto, ))
  valorFixo = cursor.fetchone()
  preço = int(valorFixo[0]) 
  
def atualizar():
  idProduto = int(input("Digite o ID do produto a ser atualizado:\n"))
  print(f"o valor é {idProduto}")
  
  campoAtualizar = (input("\nQual campo você quer atualizar ?\n[1] - Nome [2] - Categoria [3] - Refrigerado [4] - Alcoolico [5] - Quantidade [6] - Valor\n"))
  #print(f"Campo:", (campoAtualizar, ))
  campoAtualizarINT = int(campoAtualizar[0]) 
  
  atualizacao = input("Qual atualização você deseja fazer?\n")
  
  if campoAtualizarINT == 1:
    
     #print("teste1")
     cursor.execute(f"UDPATE produtos SET nomeProduto = ? WHERE ID = ?", (atualizacao, idProduto, ))
     testeNome = print(cursor.fetchall())   
     #print("teste")
     testeNome


# processo = int(input("Qual e o processo a ser feito ?\n[1] - Somar compras\n[2] - Inserir produto novo\n[3] - Consultar preço do produto\n[4] - Atualizar campo\n")) 
processo = 4

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
  print("Produto inserido com sucesso!\n")
  
if processo == 3:
  consultarPreco() 
  print(f"O valor desse produto é: R${preço}")

if processo == 4:
  atualizar()