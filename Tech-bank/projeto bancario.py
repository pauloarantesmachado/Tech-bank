create_options ="""
              Criação de conta/ Criação de Usuário/ Login
[U] Criar Usuário
[C] Criar Contas
[L] Login
"""

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
list_users = [{ "email":"claudio@legal.com", "name":"Claudio Silva", "date_of_birth":"08/07/06", "cpf":"44444444444", "location":{"adress":"rua Major", "neighborhood":"santo abacaxi", "city":"jacareí/sp" }}]
list_account = [{"user":"claudio@legal.com","agency":"0001", "account_number":0}]
accountant = 0

def create_users(email, name, date, cpf, address, neighborhood, city):
  global list_users
  for list_valid in list_users:
    if  cpf in list_valid["cpf"]:
      print("Cpf já cadastrado")
      break
    else:
      list_users.append({ "email":email, "name":name, "date_of_birth":date, "cpf": cpf, "location":{"adress":address, "neighborhood":neighborhood, "city":city }})
      print("Cadastro realizado")
      break

def creat_account(user):
  global accountant, list_account
  accountant+=1
  agency = "0001"
  account = accountant
  list_account.append({"user":user,"agency": agency, "account_number":account})
  print(f"conta criada para o usuario {user}")
 
def deposit(deposit, list_deposit):
  global balance
  if deposit > 0:
    balance+= input_money_deposit
    list_deposit.append(input_money_deposit)

    print("Deposito Realizado com Sucesso!".center(60,"*"))

  elif deposit == 0:
   return
  
  else:

    print("Por gentileza Deposite o valor corretamente!\n Escolha a opçao novamente:")
   
def withdraw(withdraw, withdrawal_limit, list_withdrawal):
    global balance, amount_of_loot
    if withdraw > balance:

      print("Não é possivel realizar o saque por falta de saldo!".center(60,"*"))
    
    elif withdraw > 500:

      print("O Limite por saque é de R$500.00!".center(60,"*"))

    elif amount_of_loot == withdrawal_limit:

      print("Somente é permitido realizar três saques diarios!".center(60,"*"))

    elif withdraw == 0:
      return
    else:
      amount_of_loot +=1
      balance -=withdraw
      print(balance)
      list_withdrawal.append(withdraw)
      print("Saque realizado com sucesso".center(60,"*"))

def bank_statement(list_deposit, list_withdrawal, balance):
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



while True:
  input_options_account = input(f"{create_options}").upper()

  if input_options_account == "U":
    email =input("Digite Teu Email:\n")
    name = input("Digite Teu nome completo:\n ")
    date_of_birth = input("Digite a Data de nascimento utlizando barra:\n Exemplo: 00/00/00 :\n ")
    cpf = input("Digite o Número do CPF sem a utilização de pontos\n Exemplo: 00000000000 :\n ")
    address = input("Digite teu endereço:\n")
    neighborhood = input("Digite teu Bairro:\n")
    city = input("Digite tua cidade/estado\n Exemplo: Belo horizonte/MG \n:")
    create_users(email=email, name=name, date=date_of_birth, cpf=cpf, address=address, neighborhood=neighborhood, city=city)


  elif input_options_account ==  "C":
    user = input("Qual o Teu email ?:\n")
    for users_list in list_users:
      login_account = users_list["email"] 
    if user in login_account:
      creat_account(user=user)
    else:
      print("usuario não existe")
     

  elif input_options_account == "L":
    login = input("Qual o teu email?\n")
    for account in list_account:
      account_list_user = account["user"]
    if login in account_list_user:
      while True:
        input_options = input(f"{options}").upper()

        if input_options == "D":

          input_money_deposit = float(input("Qual O valor para o Deposito?\nCaso queira voltar para o menu inicial escolha o numero [0]: "))
          deposit(input_money_deposit, list_deposit)
          
        elif input_options == "S":

          input_money_withdraw = float(input("Qual valor deseja Sacar?\nCaso queira voltar para o menu inicial escolha o numero [0]:\n"))
          withdraw(withdraw = input_money_withdraw, withdrawal_limit=withdrawal_limit, list_withdrawal=list_withdrawal )

        elif input_options =="E":
          bank_statement(list_deposit, list_withdrawal, balance=balance)
          
        elif input_options =="Q":

          break
    else:
      print("conta não existe")    

  else:

    print("Digite a opção corretamente".center(60,"*"))
  

    



      

    
