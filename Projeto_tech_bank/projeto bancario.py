options = """
              Escolha a opção
[S] Sacar
[D] Depositar
[E] Extrato
[Q] Sair
"""
balance = 1000
amount_of_loot = 0
withdrawal_limit = 3
list_deposit = []
list_withdrawal = []

while True:

  input_options = input(f"{options}").upper()

  if input_options == "D":

    input_money_deposit = float(input("Qual O valor para o Deposito?\nCaso queira voltar para o menu inicial escolha o numero [0]: "))
    while True:
      if input_money_deposit > 0:

        balance += input_money_deposit
        list_deposit.append(input_money_deposit)

        print("Deposito Realizado com Sucesso!".center(60,"*"))
        break

      elif input_money_deposit == 0:
        break
      else:

        print("Por gentileza Deposite o valor corretamente!\n Escolha a opçao novamente:")
        break

  elif input_options == "S":

    input_money_withdraw = float(input("Qual valor deseja Sacar?\nCaso queira voltar para o menu inicial escolha o numero [0]:\n"))
    
    while True:

      if input_money_withdraw > balance:

        print("Não é possivel realizar o saque por falta de saldo!".center(60,"*"))
        break
      
      elif input_money_withdraw > 500:

        print("O Limite por saque é de R$500.00!".center(60,"*"))
        break

      elif amount_of_loot == withdrawal_limit:

        print("Somente é permitido realizar três saques diarios!".center(60,"*"))
        break

      elif input_money_withdraw == 0:
        break

      else:
        amount_of_loot +=1
        balance -=input_money_withdraw
        list_withdrawal.append(input_money_withdraw)
        print("Saque realizado com sucesso".center(60,"*"))
        break

  elif input_options =="E":
    
    print("EXTRATO".center(60,"#"))
    print()
    print("DEPOSITOS".center(60,"-"))
    for deposit in list_deposit:
      print(f"+ R${deposit:.2f}")
    print()
    print("SAQUES".center(60,"-"))
    for withdrawal in list_withdrawal:
      print(f"- R${withdrawal:.2f}")
    print()
    print(f"""
                                                  Saldo:R${balance:.2f}""")
    
  elif input_options =="Q":

    break
  else:

    print("Digite a opção corretamente".center(60,"*"))
  

    



      

    
