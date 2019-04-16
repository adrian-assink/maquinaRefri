contador = "s"
cocaCola = 10
sprite = 7
kuat = 4
itubaina = 2
guarana = 9
agua = 6

senhaAdm = "1234"

moeda5 = 3
moeda10 = 2
moeda25 = 0
moeda50 = 0
moeda1 = 10

cedula2 = 10
cedula5 = 10
cedula10 = 10
cedula20 = 10
cedula50 = 4
cedula100 = 1

qtdInterna = (moeda5*0.05) + (moeda10*0.10) + (moeda25*0.25) + (moeda50*0.5) + (moeda1*1) + (cedula2*2) + (cedula5*5) + (cedula10*10) + (cedula20*20) + (cedula50*50) + (cedula100*100)

while True:
  print("1 - Administrador")
  print("2 - Usuario")
  contador = "s"

  menuInicial = int(input("Selecionar item: "))

  while contador == "s":
    if menuInicial == 1:
      insertSenha = input("Digite a senha de Adm: ")
      if insertSenha == senhaAdm:
        print("1 - Modificar estoque")
        print("2 - Consultar quantidade de dinheiro da maquina")
        print("3 - Consultar estoque")
        menuAdm = int(input("Selecionar item: "))
        if menuAdm == 1:
          print("1 - Quantidade de Coca Cola: ", cocaCola)
          print("2 - Quantidade de Sprite: ", sprite)
          print("3 - Quantidade de Kuar: ", kuat)
          print("4 - Quantidade de Itubaina: ", itubaina)
          print("5 - Quantidade de Guarana: ", guarana)
          print("6 - Quantidade de Agua: ", agua)
          modificarQtd = int(input("Selecionar item: "))
          if modificarQtd == 1:
            cocaCola = int(input("Atualizar QTD de Coca Colas: "))
            print("Nova QTD de Cocas: ", cocaCola)
          elif modificarQtd == 2:
            sprite = int(input("Atualizar QTD de Sprite: "))
            print("Nova QTD de Sprite: ", sprite)
          elif modificarQtd == 3:
            sprite = int(input("Atualizar QTD de Kuat: "))
            print("Nova QTD de Kuat: ", kuat)
          elif modificarQtd == 4:
            sprite = int(input("Atualizar QTD de Itubaina: "))
            print("Nova QTD de Itubaina: ", itubaina)
          elif modificarQtd == 5:
            sprite = int(input("Atualizar QTD de Guarana: "))
            print("Nova QTD de Guarana: ", guarana)
          elif modificarQtd == 6:
            sprite = int(input("Atualizar QTD de Agua: "))
            print("Nova QTD de Agua: ", agua)
          else:
            print("Comando nao reconhecido")
            contador = "n"
        elif menuAdm == 2:
          print("Quantidade total interna: R$ ", qtdInterna)
          print("1 - Quantidade de moedas: ")
          print("2 - Quantidade de cedulas: ")
          menuDinheiro = int(input("Selecionar item: "))
          if menuDinheiro == 1:
            print("1 - Qtd de moedas de 5: ", moeda5)
            print("2 - Qtd de moedas de 10: ", moeda10)
            print("3 - Qtd de moedas de 25: ", moeda25)
            print("4 - Qtd de moedas de 50: ", moeda50)
            print("5 - Qtd de cedulas de 1: ", moeda1)
          elif menuDinheiro == 2:
            print("1 - Qtd de cedulas de 2: ", cedula2)
            print("2 - Qtd de cedulas de 5: ", cedula5)
            print("3 - Qtd de cedulas de 10: ", cedula10)
            print("4 - Qtd de cedulas de 20: ", cedula20)
            print("5 - Qtd de cedulas de 50: ", cedula50)
            print("6 - Qtd de cedulas de 100: ", cedula100)
          else:
            print("Comando nao reconhecido")
            contador = "n"
        elif menuAdm == 3:
          print("Quantidade de Coca Cola: ", cocaCola)
          print("Quantidade de Sprite: ", sprite)
          print("Quantidade de Kuat: ", kuat)
          print("Quantidade de Itubaina: ", itubaina)
          print("Quantidade de Guarana: ", guarana)
          print("Quantidade de Agua: ", agua)
        else:
          print("Comando nao reconhecido")
          contador = "n"
      else:
        print("Senha incorreta")
        contador = "n"
      contador = input("Deseja fazer mais uma operação? (s/n): ")
    elif menuInicial == 2:
      print("1 - Coca Cola")
      print("2 - Sprite")
      print("3 - Kuat")
      print("4 - Itubaina")
      print("5 - Guarana")
      print("6 - Agua")
      menuSelecao = int(input("Selecionar Refri: "))

      if menuSelecao == 1:
        print("Valor Coca Cola R$4,50")
        valorItem = 4.5
        qtdRecebida = float(input("Insira o dinheiro = "))
        if cocaCola > 0:
          if qtdRecebida == valorItem:
            print("Retirar seu item")
            cocaCola = cocaCola - 1
          elif qtdRecebida < valorItem:
            print("Valor menor do que item escolhido")
          elif qtdRecebida > qtdInterna:
            print("Saldo da maquina insuficiente")
          else:
            troco = qtdRecebida - valorItem
            if troco >= 0:
              while troco >= 10:
                if cedula10 > 0:
                  troco -= 10
                  cedula10 -= 1
                  print("Cai uma cedula de R$10,00")
                else:
                  break
              while troco >= 5:
                if cedula5 > 0:
                  troco -= 5
                  cedula5 -= 1
                  print("Cai uma cedula de R$5,00")
                else:
                  break
              while troco >= 2:
                if cedula2 > 0:
                  troco -= 2
                  cedula2 -= 1
                  print("Cai uma cedula de R$2,00")
                else:
                  break
              while troco >= 1:
                if moeda1 > 0:
                  troco -= 1
                  moeda1 -= 1
                  print("Cai uma moeda de R$1,00")
                else:
                  break
              while troco >= 0.5:
                if moeda50 > 0:
                  troco -= 0.5
                  moeda50 -= 1
                  print("Cai uma moeda de R$0,50")
                else:
                  break
              while troco >= 0.25:
                if moeda25 > 0:
                  troco -= 0.25
                  moeda25 -= 1
                  print("Cai uma moeda de R$0,25")
                else:
                  break
              while troco >= 0.10:
                if moeda10 > 0:
                  troco -= 0.10
                  moeda10 -= 1
                  print("Cai uma moeda de R$0,10")
                else:
                  break
              while troco >= 0.05:
                if moeda5 > 0:
                  troco -= 0.05
                  moeda5 -= 1
                  print("Cai uma moeda de R$0,05")
                else:
                  print("Acabou o troco, chamar administrador")
                  print("Devolvendo dinheiro", round(troco, 3))
                  break
              else:
                print("Retire seu troco")
            if troco == 0:
              cocaCola = cocaCola - 1
              print("Quantidade de Coca Cola restante: ", cocaCola)
        else:
          print("Item fora de estoque, devolvendo dinheiro")
        contador = input("Deseja fazer mais uma operação? (s/n): ")

      elif menuSelecao == 2:
        print("Valor Sprite R$3,50")
        valorItem = 3.5
        qtdRecebida = float(input("Insira o dinheiro = "))
        if sprite > 0:
          if qtdRecebida == valorItem:
            print("Retirar seu item")
            sprite = sprite - 1
          elif qtdRecebida < valorItem:
            print("Valor menor do que item escolhido")
          elif qtdRecebida > qtdInterna:
            print("Saldo da maquina insuficiente")
          else:
            troco = qtdRecebida - valorItem
            if troco >= 0:
              while troco >= 10:
                if cedula10 > 0:
                  troco -= 10
                  cedula10 -= 1
                  print("Cai uma cedula de R$10,00")
                else:
                  break
              while troco >= 5:
                if cedula5 > 0:
                  troco -= 5
                  cedula5 -= 1
                  print("Cai uma cedula de R$5,00")
              while troco >= 2:
                if cedula2 > 0:
                  troco -= 2
                  cedula2 -= 1
                  print("Cai uma cedula de R$2,00")
                else:
                  break
              while troco >= 1:
                if moeda1 > 0:
                  troco -= 1
                  moeda1 -= 1
                  print("Cai uma moeda de R$1,00")
                else:
                  break
              while troco >= 0.5:
                if moeda50 > 0:
                  troco -= 0.5
                  moeda50 -= 1
                  print("Cai uma moeda de R$0,50")
                else:
                  break
              while troco >= 0.25:
                if moeda25 > 0:
                  troco -= 0.25
                  moeda25 -= 1
                  print("Cai uma moeda de R$0,25")
                else:
                  break
              while troco >= 0.10:
                if moeda10 > 0:
                  troco -= 0.10
                  moeda10 -= 1
                  print("Cai uma moeda de R$0,10")
              while troco >= 0.05:
                if moeda5 > 0:
                  troco -= 0.05
                  moeda5 -= 1
                  print("Cai uma moeda de R$0,05")
                else:
                  print("Acabou o troco, chamar administrador")
                  print("Devolvendo dinheiro", round(troco, 3))
                  break
              else:
                print("Retire seu troco")
            if troco == 0:
              sprite = sprite - 1
              print("Quantidade de Sprite restante: ", sprite)
        else:
          print("Item fora de estoque, devolvendo dinheiro")
        contador = input("Deseja fazer mais uma operação? (s/n): ")

      elif menuSelecao == 3:
        print("Valor Kuat R$3,50")
        valorItem = 3.5
        qtdRecebida = float(input("Insira o dinheiro = "))
        if kuat > 0:
          if qtdRecebida == valorItem:
            print("Retirar seu item")
            kuat = kuat - 1
          elif qtdRecebida < valorItem:
            print("Valor menor do que item escolhido")
          elif qtdRecebida > qtdInterna:
            print("Saldo da maquina insuficiente")
          else:
            troco = qtdRecebida - valorItem
            if troco >= 0:
              while troco >= 10:
                if cedula10 > 0:
                  troco -= 10
                  cedula10 -= 1
                  print("Cai uma cedula de R$10,00")
                else:
                  break
              while troco >= 5:
                if cedula5 > 0:
                  troco -= 5
                  cedula5 -= 1
                  print("Cai uma cedula de R$5,00")
                else:
                  break
              while troco >= 2:
                if cedula2 > 0:
                  troco -= 2
                  cedula2 -= 1
                  print("Cai uma cedula de R$2,00")
                else:
                  break
              while troco >= 1:
                if moeda1 > 0:
                  troco -= 1
                  moeda1 -= 1
                  print("Cai uma moeda de R$1,00")
                else:
                  break
              while troco >= 0.5:
                if moeda50 > 0:
                  troco -= 0.5
                  moeda50 -= 1
                  print("Cai uma moeda de R$0,50")
                else:
                  break
              while troco >= 0.25:
                if moeda25 > 0:
                  troco -= 0.25
                  moeda25 -= 1
                  print("Cai uma moeda de R$0,25")
                else:
                  break
              while troco >= 0.10:
                if moeda10 > 0:
                  troco -= 0.10
                  moeda10 -= 1
                  print("Cai uma moeda de R$0,10")
                else:
                  break
              while troco >= 0.05:
                if moeda5 > 0:
                  troco -= 0.05
                  moeda5 -= 1
                  print("Cai uma moeda de R$0,05")
                else:
                  print("Acabou o troco, chamar administrador")
                  print("Devolvendo dinheiro", round(troco, 3))
                  break
              else:
                print("Retire seu troco")
            if troco == 0:
              kuat = kuat - 1
              print("Quantidade de Kuat restante: ", kuat)
        else:
          print("Item fora de estoque, devolvendo dinheiro")
        contador = input("Deseja fazer mais uma operação? (s/n): ")

      elif menuSelecao == 4:
        print("Valor Itubaina R$2,50")
        valorItem = 2.5
        qtdRecebida = float(input("Insira o dinheiro = "))
        if itubaina > 0:
          if qtdRecebida == valorItem:
            print("Retirar seu item")
            itubaina = itubaina - 1
          elif qtdRecebida < valorItem:
            print("Valor menor do que item escolhido")
          elif qtdRecebida > qtdInterna:
            print("Saldo da maquina insuficiente")
          else:
            troco = qtdRecebida - valorItem
            if troco >= 0:
              while troco >= 10:
                if cedula10 > 0:
                  troco -= 10
                  cedula10 -= 1
                  print("Cai uma cedula de R$10,00")
                else:
                  break
              while troco >= 5:
                if cedula5 > 0:
                  troco -= 5
                  cedula5 -= 1
                  print("Cai uma cedula de R$5,00")
                else:
                  break
              while troco >= 2:
                if cedula2 > 0:
                  troco -= 2
                  cedula2 -= 1
                  print("Cai uma cedula de R$2,00")
                else:
                  break
              while troco >= 1:
                if moeda1 > 0:
                  troco -= 1
                  moeda1 -= 1
                  print("Cai uma moeda de R$1,00")
                else:
                  break
              while troco >= 0.5:
                if moeda50 > 0:
                  troco -= 0.5
                  moeda50 -= 1
                  print("Cai uma moeda de R$0,50")
                else:
                  break
              while troco >= 0.25:
                if moeda25 > 0:
                  troco -= 0.25
                  moeda25 -= 1
                  print("Cai uma moeda de R$0,25")
                else:
                  break
              while troco >= 0.10:
                if moeda10 > 0:
                  troco -= 0.10
                  moeda10 -= 1
                  print("Cai uma moeda de R$0,10")
                else:
                  break
              while troco >= 0.05:
                if moeda5 > 0:
                  troco -= 0.05
                  moeda5 -= 1
                  print("Cai uma moeda de R$0,05")
                else:
                  print("Acabou o troco, chamar administrador")
                  print("Devolvendo dinheiro", round(troco, 3))
                  break
              else:
                print("Retire seu troco")
            if troco == 0:
              itubaina = itubaina - 1
              print("Quantidade de Kuat restante: ", itubaina)
        else:
          print("Item fora de estoque, devolvendo dinheiro")
        contador = input("Deseja fazer mais uma operação? (s/n): ")
      
      elif menuSelecao == 5:
        print("Valor Guarana R$3,00")
        valorItem = 3.0
        qtdRecebida = float(input("Insira o dinheiro = "))
        if guarana > 0:
          if qtdRecebida == valorItem:
            print("Retirar seu item")
            guarana = guarana - 1
          elif qtdRecebida < valorItem:
            print("Valor menor do que item escolhido")
          elif qtdRecebida > qtdInterna:
            print("Saldo da maquina insuficiente")
          else:
            troco = qtdRecebida - valorItem
            if troco >= 0:
              while troco >= 10:
                if cedula10 > 0:
                  troco -= 10
                  cedula10 -= 1
                  print("Cai uma cedula de R$10,00")
                else:
                  break
              while troco >= 5:
                if cedula5 > 0:
                  troco -= 5
                  cedula5 -= 1
                  print("Cai uma cedula de R$5,00")
                else:
                  break
              while troco >= 2:
                if cedula2 > 0:
                  troco -= 2
                  cedula2 -= 1
                  print("Cai uma cedula de R$2,00")
                else:
                  break
              while troco >= 1:
                if moeda1 > 0:
                  troco -= 1
                  moeda1 -= 1
                  print("Cai uma moeda de R$1,00")
                else:
                  break
              while troco >= 0.5:
                if moeda50 > 0:
                  troco -= 0.5
                  moeda50 -= 1
                  print("Cai uma moeda de R$0,50")
                else:
                  break
              while troco >= 0.25:
                if moeda25 > 0:
                  troco -= 0.25
                  moeda25 -= 1
                  print("Cai uma moeda de R$0,25")
                else:
                  break
              while troco >= 0.10:
                if moeda10 > 0:
                  troco -= 0.10
                  moeda10 -= 1
                  print("Cai uma moeda de R$0,10")
                else:
                  break
              while troco >= 0.05:
                if moeda5 > 0:
                  troco -= 0.05
                  moeda5 -= 1
                  print("Cai uma moeda de R$0,05")
                else:
                  print("Acabou o troco, chamar administrador")
                  print("Devolvendo dinheiro", round(troco, 3))
                  break
              else:
                print("Retire seu troco")
            if troco == 0:
              guarana = guarana - 1
              print("Quantidade de Kuat restante: ", guarana)
        else:
          print("Item fora de estoque, devolvendo dinheiro")
        contador = input("Deseja fazer mais uma operação? (s/n): ")
      
      elif menuSelecao == 6:
        print("Valor Agua R$3,00")
        valorItem = 3.0
        qtdRecebida = float(input("Insira o dinheiro = "))
        if agua > 0:
          if qtdRecebida == valorItem:
            print("Retirar seu item")
            agua = agua - 1
          elif qtdRecebida < valorItem:
            print("Valor menor do que item escolhido")
          elif qtdRecebida > qtdInterna:
            print("Saldo da maquina insuficiente")
          else:
            troco = qtdRecebida - valorItem
            if troco >= 0:
              while troco >= 10:
                if cedula10 > 0:
                  troco -= 10
                  cedula10 -= 1
                  print("Cai uma cedula de R$10,00")
                else:
                  break
              while troco >= 5:
                if cedula5 > 0:
                  troco -= 5
                  cedula5 -= 1
                  print("Cai uma cedula de R$5,00")
                else:
                  break
              while troco >= 2:
                if cedula2 > 0:
                  troco -= 2
                  cedula2 -= 1
                  print("Cai uma cedula de R$2,00")
                else:
                  break
              while troco >= 1:
                if moeda1 > 0:
                  troco -= 1
                  moeda1 -= 1
                  print("Cai uma moeda de R$1,00")
                else:
                  break
              while troco >= 0.5:
                if moeda50 > 0:
                  troco -= 0.5
                  moeda50 -= 1
                  print("Cai uma moeda de R$0,50")
                else:
                  break
              while troco >= 0.25:
                if moeda25 > 0:
                  troco -= 0.25
                  moeda25 -= 1
                  print("Cai uma moeda de R$0,25")
                else:
                  break
              while troco >= 0.10:
                if moeda10 > 0:
                  troco -= 0.10
                  moeda10 -= 1
                  print("Cai uma moeda de R$0,10")
                else:
                  break
              while troco >= 0.05:
                if moeda5 > 0:
                  troco -= 0.05
                  moeda5 -= 1
                  print("Cai uma moeda de R$0,05")
                else:
                  print("Acabou o troco, chamar administrador")
                  print("Devolvendo dinheiro", round(troco, 3))
                  break
              else:
                print("Retire seu troco")
            if troco == 0:
              agua = agua - 1
              print("Quantidade de Kuat restante: ", agua)
        else:
          print("Item fora de estoque, devolvendo dinheiro")
        contador = input("Deseja fazer mais uma operação? (s/n): ")
      else:
        print("Comando nao reconhecido")
        contador = "n"
    else:
     print("Comando nao reconhecido")
     contador = "n"
