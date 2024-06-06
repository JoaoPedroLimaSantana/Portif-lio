import mysql.connector

# conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789',
    database='mercadodojoao',
)

cursor = conexao.cursor()
while True:
   qual_tabela = input("qual tabela deseja operar? ")
   if qual_tabela == "produtos":
        while True:
            operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
            if operacao == "c":

                #CREATE
                    produtos = input("qual produto deseja adicionar ao banco de dados? ")
                    valor = int(input("qual o valor? "))
                    comando = f'INSERT INTO produtos (produtos, valor) VALUES ("{produtos}", {valor})'
                    cursor.execute(comando)
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    break


            if operacao == "r":

                #READ
                    print("lendo o banco de dados")
                    comando = f'SELECT * FROM produtos'
                    cursor.execute(comando)
                    resultado = cursor.fetchall() # ler o banco de dados
                    print(resultado)
                    cursor.close()
                    conexao.close()
                    break

            if operacao == "u":

                    #UPDATE
                    produtos = input("qual produto deseja mudar o valor? ")
                    valor = int(input("qual o valor?"))
                    comando = f'UPDATE produtos SET valor = {valor} WHERE produtos = "{produtos}"'
                    cursor.execute(comando)
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    break


            if operacao == "d":

                    #DELETE
                    produtos = input("qual produto deseja deletar do banco de dados?")
                    comando = f'DELETE FROM produtos WHERE produtos = "{produtos}"'
                    cursor.execute(comando)
                    conexao.commit()  # edita o banco de dados
                    cursor.close()
                    conexao.close()
                    break

   if qual_tabela == "funccaixa":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

                   # CREATE
                   cpf = int(input("qual o CPF do funcionário? "))
                   nome = input("qual o nome? ")
                   comando = f'INSERT INTO funccaixa (cpf, nome) VALUES ({cpf}, "{nome}")'
                   cursor.execute(comando)
                   conexao.commit()
                   cursor.close()
                   conexao.close()
                   fechar = input("aperte ENTER para fechar")
                   if fechar == "":
                    break


           if operacao == "r":

                   # READ
                   print("lendo o banco de dados")
                   comando = f'SELECT * FROM funccaixa'
                   cursor.execute(comando)
                   resultado = cursor.fetchall()  # ler o banco de dados
                   print(resultado)
                   cursor.close()
                   conexao.close()
                   break

           if operacao == "u":

                   # UPDATE
                   idfunccaixa = input("qual o id para mudar o nome? ")
                   nome = (input("qual o nome? "))
                   comando = f'UPDATE funccaixa SET nome = {nome} WHERE idfunccaixa = "{idfunccaixa}"'
                   cursor.execute(comando)
                   conexao.commit()
                   cursor.close()
                   conexao.close()
                   break


           if operacao == "d":

                   # DELETE
                   id = input("qual o id de quem vai para a rua? ")
                   comando = f'DELETE FROM funccaixa WHERE idfunccaixa = "{id}"'
                   cursor.execute(comando)
                   conexao.commit()  # edita o banco de dados
                   cursor.close()
                   conexao.close()
                   break
               #ta perdio essa porra aqui mds do ceu
   if qual_tabela == "funcacougue":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

                   # CREATE
                   cpf = int(input("qual o CPF do funcionário? "))
                   nome = input("qual o nome? ")
                   comando = f'INSERT INTO funcacougue (cpf, nome) VALUES ({cpf}, "{nome}")'
                   cursor.execute(comando)
                   conexao.commit()
                   cursor.close()
                   conexao.close()
                   fechar = input("aperte ENTER para fechar")
                   if fechar == "":
                    break


           if operacao == "r":

                   # READ
                   print("lendo o banco de dados")
                   comando = f'SELECT * FROM funcacougue'
                   cursor.execute(comando)
                   resultado = cursor.fetchall()  # ler o banco de dados
                   print(resultado)
                   cursor.close()
                   conexao.close()
                   break

           if operacao == "u":

                   # UPDATE
                   idfuncacougue = input("qual o id para mudar o nome? ")
                   nome = (input("qual o nome? "))
                   comando = f'UPDATE funcacougue SET nome = {nome} WHERE idfuncacougue = "{idfuncacougue}"'
                   cursor.execute(comando)
                   conexao.commit()
                   cursor.close()
                   conexao.close()
                   break


           if operacao == "d":

                   # DELETE
                   id = input("qual o id de quem vai para a rua? ")
                   comando = f'DELETE FROM funcacougue WHERE funcacougue = "{id}"'
                   cursor.execute(comando)
                   conexao.commit()  # edita o banco de dados
                   cursor.close()
                   conexao.close()
                   break
   if qual_tabela == "funclimp":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE
               cpf = int(input("qual o CPF do funcionário? "))
               nome = input("qual o nome? ")
               comando = f'INSERT INTO funclimp (cpf, nome) VALUES ({cpf}, "{nome}")'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM funclimp'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idfunclimp = input("qual o id para mudar o nome? ")
               nome = (input("qual o nome? "))
               comando = f'UPDATE funclimp SET nome = {nome} WHERE idfunclimp = "{idfunclimp}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id de quem vai para a rua? ")
               comando = f'DELETE FROM funclimp WHERE funclimp = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "funcgerente":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE
               cpf = int(input("qual o CPF do funcionário? "))
               nome = input("qual o nome? ")
               comando = f'INSERT INTO funcgerente (cpf, nome) VALUES ({cpf}, "{nome}")'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM funcgerente'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idfuncgerente = input("qual o id para mudar o nome? ")
               nome = (input("qual o nome? "))
               comando = f'UPDATE funcgerente SET nome = {nome} WHERE idfuncgerente = "{idfuncgerente}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id de quem vai para a rua? ")
               comando = f'DELETE FROM funcgerente WHERE funcgerente = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "funcmrk": #funcionario de marketing
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE
               cpf = int(input("qual o CPF do funcionário? "))
               nome = input("qual o nome? ")
               comando = f'INSERT INTO funcmrk (cpf, nome) VALUES ({cpf}, "{nome}")'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM funcmrk'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idfuncmrk = input("qual o id para mudar o nome? ")
               nome = (input("qual o nome? "))
               comando = f'UPDATE funcmrk SET nome = {nome} WHERE idfuncmrk = "{idfuncmrk}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id de quem vai para a rua? ")
               comando = f'DELETE FROM funcmrk WHERE funcmrk = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "cartaocliente":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE
               nome = input("qual o nome? ")
               saldo = int(input("qual o saldo do cliente? "))
               comando = f'INSERT INTO cartaocliente (nome, saldo) VALUES ("{nome}", {saldo})'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM cartaocliente'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idcartaocliente = input("qual o id para mudar o saldo? ")
               saldo = (input("qual o novo saldo? "))
               comando = f'UPDATE cartaocliente SET nome = {saldo} WHERE cartaocliente = "{idcartaocliente}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id do cliente? ")
               comando = f'DELETE FROM idcartaocliente WHERE idcartaocliente = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "fornecedor1":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE

               saldo = input("o que ele fornece? ")
               comando = f'INSERT INTO fornecedor1 (mercadoria) VALUES ("{saldo}")'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM fornecedor1'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idcartaocliente = input("qual o id para mudar a mercadoria? ")
               saldo = (input("qual a nova mercadoria? "))
               comando = f'UPDATE fornecedor1 SET nome = {saldo} WHERE fornecedor1 = "{idcartaocliente}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id da mercadoria? ")
               comando = f'DELETE FROM fornecedor1 WHERE fornecedor1 = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "fornecedor2":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE

               saldo = input("o que ele fornece? ")
               comando = f'INSERT INTO fornecedor2 (mercadoria) VALUES ("{saldo}")'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM fornecedor2'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idcartaocliente = input("qual o id para mudar a mercadoria? ")
               saldo = (input("qual a nova mercadoria? "))
               comando = f'UPDATE fornecedor2 SET nome = {saldo} WHERE fornecedor2 = "{idcartaocliente}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id da mercadoria? ")
               comando = f'DELETE FROM fornecedor2 WHERE fornecedor2 = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "fornecedor3":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE

               saldo = input("o que ele fornece? ")
               comando = f'INSERT INTO fornecedor3 (mercadoria) VALUES ("{saldo}")'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM fornecedor3'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idcartaocliente = input("qual o id para mudar a mercadoria? ")
               saldo = (input("qual a nova mercadoria? "))
               comando = f'UPDATE fornecedor3 SET nome = {saldo} WHERE fornecedor3 = "{idcartaocliente}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id da mercadoria? ")
               comando = f'DELETE FROM fornecedor3 WHERE fornecedor3 = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "fornecedor4":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE

               saldo = input("o que ele fornece? ")
               comando = f'INSERT INTO fornecedor4 (mercadoria) VALUES ("{saldo}")'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM fornecedor4'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idcartaocliente = input("qual o id para mudar a mercadoria? ")
               saldo = (input("qual a nova mercadoria? "))
               comando = f'UPDATE fornecedor4 SET nome = {saldo} WHERE fornecedor4 = "{idcartaocliente}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id da mercadoria? ")
               comando = f'DELETE FROM fornecedor4 WHERE fornecedor4 = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "fornecedor5":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE

               saldo = input("o que ele fornece? ")
               comando = f'INSERT INTO fornecedor5 (mercadoria) VALUES ("{saldo}")'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM fornecedor5'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idcartaocliente = input("qual o id para mudar a mercadoria? ")
               saldo = (input("qual a nova mercadoria? "))
               comando = f'UPDATE fornecedor5 SET nome = {saldo} WHERE fornecedor5 = "{idcartaocliente}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id da mercadoria? ")
               comando = f'DELETE FROM fornecedor5 WHERE fornecedor5 = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break
   if qual_tabela == "financeiro":
       while True:
           operacao = input("o que deseja executar no banco de dados? (C/R/U/D) ")
           if operacao == "c":

               # CREATE

               saldo = int(input("qual o faturamento do dia? "))
               dia = input("que dia é hoje? ")
               comando = f'INSERT INTO financeiro (dinheiros, dia) VALUES ("{saldo}", {dia})'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               fechar = input("aperte ENTER para fechar")
               if fechar == "":
                   break

           if operacao == "r":
               # READ
               print("lendo o banco de dados")
               comando = f'SELECT * FROM financeiro'
               cursor.execute(comando)
               resultado = cursor.fetchall()  # ler o banco de dados
               print(resultado)
               cursor.close()
               conexao.close()
               break

           if operacao == "u":
               # UPDATE
               idfinanceiro = input("qual o id para mudar o faturamento? ")
               saldo = (input("qual o novo faturamento? "))
               comando = f'UPDATE dinheiros SET nome = {saldo} WHERE idfinanceiro = "{idfinanceiro}"'
               cursor.execute(comando)
               conexao.commit()
               cursor.close()
               conexao.close()
               break

           if operacao == "d":
               # DELETE
               id = input("qual o id da mercadoria? ")
               comando = f'DELETE FROM financeiro WHERE financeiro = "{id}"'
               cursor.execute(comando)
               conexao.commit()  # edita o banco de dados
               cursor.close()
               conexao.close()
               break












   else:
       print("não tem uma tabela com esse nome")
       fechar = input("tentar novamente? (s/n) ")
       if fechar == "s":
           continue
       else:
           break
