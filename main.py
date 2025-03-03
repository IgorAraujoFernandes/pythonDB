import sqlite3
import os

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


  global valorFixo
  IDproduto = int(input("Digite o ID do produto a ser consultado:\n"))
  cursor.execute("SELECT valorFixo FROM produtos WHERE ID = ?", (IDproduto,))
  novoValorFixo = cursor.fetchone() 
  valorFixo = int(novoValorFixo[0])
  
 
def atualizar():
  idProduto = int(input("Digite o ID do produto a ser atualizado:\n"))
  print(f"o valor é {idProduto}")
  
  campoAtualizar = (input("\nQual campo você quer atualizar ?\n[1] - Nome [2] - Categoria [3] - Refrigerado [4] - Alcoolico [5] - Quantidade [6] - Valor\n"))
  campoAtualizarINT = int(campoAtualizar) 
  
  if campoAtualizarINT == 3 or campoAtualizarINT == 4:
    try:
      binario = int(input("Escolha o status:\n[1] - Refrigerado    [2] - Não refrigerado\n"))
    except ValueError:
      print("Numero inválido\n")
    if binario == 2:
      binario = 0
  else:
     atualizacao = input("Qual atualização você deseja fazer?\n")
     if campoAtualizarINT == 5 or campoAtualizarINT == 6:
      try:
        atualizacaoint= int(atualizacao)
      except ValueError:
        print("Valor inválido\n")
  if campoAtualizarINT == 1:
    
     cursor.execute("UPDATE produtos SET nomeProduto = ? WHERE ID = ?", (atualizacao, idProduto, ))
     banco.commit()
     cursor.execute("SELECT * FROM produtos WHERE ID = ?", (idProduto, ))
     print(cursor.fetchone())
   
  
  if campoAtualizarINT == 2:
    
     cursor.execute("UPDATE produtos SET categoria = ? WHERE ID = ?", (atualizacao, idProduto, ))
     banco.commit()
     cursor.execute("SELECT * FROM produtos WHERE ID = ?", (idProduto, ))
     print(cursor.fetchone())
   
  if campoAtualizarINT == 3 or campoAtualizarINT == 4:
    
    if campoAtualizarINT == 3:
      cursor.execute("UPDATE produtos SET refrigerado = ? WHERE ID = ?", (binario, idProduto, )) 
    else:
      cursor.execute("UPDATE produtos SET alcoolico = ? WHERE ID = ?", (binario, idProduto, ))
  banco.commit()
  cursor.execute("SELECT * FROM produtos WHERE ID = ?", (idProduto, ))
  print(cursor.fetchone())
    
  if campoAtualizarINT == 5 or campoAtualizarINT == 6:
        
        if campoAtualizarINT == 5:
          cursor.execute("UPDATE produtos SET quantidade = ? WHERE ID = ?", (atualizacaoint, idProduto, ))
        else:
          cursor.execute("UPDATE produtos SET valorFixo = ? WHERE ID = ?", (atualizacaoint, idProduto))
  banco.commit()
  cursor.execute("SELECT * FROM produtos WHERE ID = ?", (idProduto, ))
  print(cursor.fetchone())      

def excluir():

  IDproduto = input("Digite o ID do produto a ser excluido:\n")
  try:
    IDproduto = int(IDproduto)
  except ValueError:
    print("Valor inválido\n")
  cursor.execute("DELETE FROM produtos WHERE ID = ?", (IDproduto, ))
  banco.commit()

def printID():
   cursor.execute('SELECT ID, nomeProduto FROM produtos')
   listaID = (cursor.fetchall())
   print(f"Os IDs sao:\n{listaID}\n")

def main():
  processo = int(input("Qual e o processo a ser feito ?\n[1] - Somar compras\n[2] - Inserir produto novo\n[3] - Consultar preço do produto\n[4] - Atualizar campo\n[5] - Excluir campo\n")) 
  if processo != 2:
    printID()
    
  if processo == 1:
         global valorProduto
         valorProduto = [limite]
         i = 0
         somaTotal = 0
         print('Digite "FIM" a qualquer momento do programa para finalizar')
          
         while i < limite:          
            
              produto = (input("Digite o ID do produto\n"))
              if produto.upper() == "FIM":
                break
              
              try:
                produto = int(produto)
              except ValueError:
                print("Por favor, insira um número válido para o ID do produto.")  
                continue
              somarCompras(produto)
              somaTotal += valorSoma
              i += 1
              print(f"O valor total da compra é:R${somaTotal}\n")
              
                                
  if processo == 2:
    inserirProduto()
    print("Produto inserido com sucesso!\n")
    
  if processo == 3:
    consultarPreco() 
    print(f"O valor desse produto é: R${valorFixo}")

  if processo == 4:
    atualizar()

  if processo == 5:
      excluir() 
  

def letreiro():
  print("---------------------------------------------------------------------------------------------------------------\n")
  print("███╗░░░███╗███████╗██████╗░░█████╗░░█████╗░██████╗░░█████╗░  ██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██\n████╗░████║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██\n██╔████╔██║█████╗░░██████╔╝██║░░╚═╝███████║██║░░██║██║░░██║  ██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██\n██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██╗██╔══██║██║░░██║██║░░██║  ██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████\n██║░╚═╝░██║███████╗██║░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝  ██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║\n")
  
  print("---------------------------------------------------------------------------------------------------------------\n")

os.system("cls")
letreiro()
main()